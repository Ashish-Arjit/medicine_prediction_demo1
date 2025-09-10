from flask import Flask, render_template, request
import pandas as pd

app = Flask(__name__)

# Load dataset once
df = pd.read_csv("demo3.csv")

# ... Include your existing classify_age_group, parse_duration, and search_medicine_multiple functions here ...
# (Copy the full code of those functions here without the input/output parts)

# Modified route to handle web requests
@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        symptoms_input = request.form.get("symptoms", "")
        age = int(request.form.get("age", 0))
        gender = request.form.get("gender", "male").lower()
        pregnancy = request.form.get("pregnancy", "no").lower()
        feeding = request.form.get("feeding", "no").lower()
        duration = request.form.get("duration", "")

        # Use modified search function that accepts duration as parameter instead of input
        output = search_medicine_web(symptoms_input, age, gender, pregnancy, feeding, duration, df)

        return render_template("index.html", result=output)

    return render_template("index.html", result=None)

def search_medicine_web(symptoms_input, age, gender, pregnancy, feeding, duration, df):
    age_group = classify_age_group(age)
    symptoms = [sym.strip().lower() for sym in symptoms_input.split(",")]
    results = []
    duration_days = parse_duration(duration)
    if duration_days > 7:
        return (f"⚠️ You are suffering for more than 1 week ({duration}).\n"
                f"➡️ Please consult a doctor for proper medical advice.")
    for symptom in symptoms:
        filtered_df = df[
            df['Symptom'].str.lower().str.contains(symptom, na=False) &
            (df['Age Group'].str.strip() == age_group)
        ]
        if filtered_df.empty:
            results.append(f"No suitable medicine found for '{symptom}' in age group '{age_group}'.")
            continue
        best = filtered_df.iloc[0]
        results.append(f"For '{symptom}' (since {duration}):\n"
                       f"Medicine: {best['Medicine']}\nDosage: {best['Dosage']}")
    if gender == "female" and age >= 18:
        if pregnancy == "yes":
            results.append("\n⚠️ Note: You mentioned pregnancy.\n"
                           "➡️ Some medicines may not be safe. Please consult a doctor before taking them.")
            if feeding == "yes":
                results.append("\n⚠️ Additional Note: You are feeding a baby.\n"
                               "➡️ Extra caution required with medicines. Doctor advice strongly recommended.")
    return "\n\n".join(results)

if __name__ == "__main__":
    app.run(debug=True)
