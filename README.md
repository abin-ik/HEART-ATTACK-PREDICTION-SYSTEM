# ❤️ Heart Attack Risk Prediction Web App

A full-stack **Machine Learning web application** that predicts the risk of a heart attack based on user-provided medical data. This project combines **ML + FastAPI backend + HTML/CSS frontend** into a complete, deployable system.

---

## 🚀 Project Overview

This application allows users to enter key medical attributes such as age, blood pressure, cholesterol level, ECG results, and more. The data is sent to a FastAPI backend where a trained **Random Forest Classifier** predicts whether the user is **Safe** or **At Risk** of a heart attack.

The goal of this project was to build an **end-to-end ML product**, not just a model — covering training, API integration, validation, and UI.

---

## 🔍 Features

* ✅ Trained a **Random Forest Classifier** on a heart disease dataset
* ✅ Clean **glassmorphism-inspired UI** using HTML & CSS
* ✅ Fully functional **FastAPI backend** with Pydantic validation
* ✅ Seamless integration: **Model → API → Frontend**
* ✅ Dynamic result page displaying:

  * `0 → Safe`
  * `1 → At Risk of Heart Attack`
* ✅ JSON-based request/response handling

---

## 🧠 Tech Stack

* **Language:** Python
* **Machine Learning:** Scikit-learn (Random Forest)
* **Backend:** FastAPI, Pydantic
* **Frontend:** HTML, CSS, Bootstrap
* **Templating:** Jinja2

---

## 💡 How It Works

1. User enters medical details via the web form
2. Frontend sends data to FastAPI using a POST request
3. FastAPI validates input using Pydantic schemas
4. Trained ML model processes the input
5. Prediction is returned and displayed on the result page

---

## 📂 Project Structure (Example)

```
├── app/
│   ├── main.py            # FastAPI app
│   ├── model.pkl          # Trained ML model (gitignored)
│   ├── schemas.py         # Pydantic models
│   └── utils.py           # Prediction logic
├── templates/
│   ├── index.html
│   └── result.html
├── static/
│   └── styles.css
├── training/
│   └── train_model.py
├── requirements.txt
├── .gitignore
└── README.md
```

---

## 🧪 Model Details

* **Algorithm:** Random Forest Classifier
* **Input:** Medical attributes (age, BP, cholesterol, ECG, etc.)
* **Output:**

  * `0` → Safe
  * `1` → Risk of Heart Attack

---

## ▶️ Running the Project Locally

```bash
# Install dependencies
pip install -r requirements.txt

# Start the FastAPI server
uvicorn app.main:app --reload
```

Then open your browser at:

```
http://127.0.0.1:8000
```

---

## 📌 Notes

* Trained model files (`.pkl`) are excluded from version control
* Focused on **clean architecture** and **real-world ML deployment** practices
* This project is intended for **learning and demonstration purposes**

---


