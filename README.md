# medicine_prediction_demo1


This Python project recommends suitable medicines and dosages based on user symptoms, age, gender, and pregnancy/feeding status using a CSV-based dataset.

## How to Run
1. Place `app.py`, `demo3.csv`, and `requirements.txt` in the same folder.
2. Install dependencies: `pip install -r requirements.txt`
3. Run: `python app.py`
4. Follow on-screen prompts for symptoms, age, gender, etc.

## Dataset Format (`demo3.csv`)
| Symptom  | Age Group     | Medicine          | Dosage          |
|----------|---------------|-------------------|-----------------|
| Fever    | Above 15 years| Paracetamol       | 500mg twice/day |
| Cough    | 6-15 years    | Dextromethorphan  | 10mg twice/day  |

## Features
- Multi-symptom input
- Age group classification
- Duration-based recommendations/warnings
- Pregnancy and feeding safety alerts

## Contributing
Pull requests welcome. Please ensure new data entries in demo3.csv follow the column format.

## License
MIT
