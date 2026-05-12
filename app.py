from fastapi import FastAPI
import pandas as pd
import joblib

app = FastAPI()

# Load trained model
model = joblib.load("model.pkl")


@app.get("/")
def home():
    return {
        "message": "Student Score Prediction API is running"
    }


@app.post("/predict")
def predict(
    gender: str,
    race_ethnicity: str,
    parental_level_of_education: str,
    lunch: str,
    test_preparation_course: str,
    reading_score: int,
    writing_score: int
):

    # Create dataframe
    data = pd.DataFrame({
        "gender": [gender],
        "race/ethnicity": [race_ethnicity],
        "parental level of education": [parental_level_of_education],
        "lunch": [lunch],
        "test preparation course": [test_preparation_course],
        "reading score": [reading_score],
        "writing score": [writing_score]
    })

    # Apply same encoding
    data = pd.get_dummies(data)

    # Expected columns from training
    expected_columns = model.feature_names_in_

    # Add missing columns
    for col in expected_columns:
        if col not in data.columns:
            data[col] = 0

    # Reorder columns
    data = data[expected_columns]

    # Predict
    prediction = model.predict(data)

    return {
        "predicted_math_score": round(prediction[0], 2)
    }