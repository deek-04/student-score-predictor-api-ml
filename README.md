# Student Score Prediction API 🚀

A Machine Learning powered REST API built using **FastAPI** and **Scikit-learn** to predict student math scores based on academic and demographic features.

This project demonstrates an end-to-end ML workflow including:

* data preprocessing
* categorical encoding
* multiple linear regression
* model evaluation
* ML model deployment using FastAPI

---

# 🛠️ Tech Stack

* Python
* FastAPI
* Scikit-learn
* Pandas
* NumPy
* Joblib
* Uvicorn

---

# 📂 Project Structure

```text id="a1"
student-ml-api/
│
├── app.py
├── student_model.pkl
├── Multiple linear regression.ipynb
├── StudentsPerformance.csv
├── requirements.txt
└── README.md
```

---

# ⚙️ Installation

## Clone Repository

```bash id="a2"
git clone <your-repository-link>
```

---

## Create Virtual Environment

```bash id="a3"
python -m venv venv
```

---

## Activate Virtual Environment

### Windows

```bash id="a4"
venv\Scripts\activate
```

---

## Install Dependencies

```bash id="a5"
pip install -r requirements.txt
```

---

# ▶️ Run FastAPI Server

```bash id="a6"
uvicorn app:app --reload
```

---

# 📖 Swagger API Documentation

Open:

```text id="a7"
http://127.0.0.1:8000/docs
```

---

# 📬 API Endpoint

| Method | Endpoint | Description                |
| ------ | -------- | -------------------------- |
| POST   | /predict | Predict student math score |

---

# 📊 Machine Learning Workflow

* Data preprocessing
* Handling categorical variables
* One-hot encoding using `pd.get_dummies()`
* Train-test split
* Multiple Linear Regression
* Model evaluation using:

  * Mean Squared Error (MSE)
  * R² Score

---

# 📈 Model Performance

* Mean Squared Error (MSE): `29.09`
* R² Score: `0.88`

The model achieved strong prediction performance on unseen test data.

---

# 🚀 Future Improvements

* Model deployment on cloud platforms
* Frontend integration
* Advanced ML models
* Authentication & user tracking
* Prediction analytics dashboard

---

# 💡 Learning Outcomes

Through this project, I learned:

* Machine Learning workflow
* Regression algorithms
* Data preprocessing
* Feature encoding
* FastAPI integration
* Model deployment basics
* REST API testing using Swagger/Postman
