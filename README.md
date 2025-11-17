Here is a **beautifully formatted, professional, GitHub-ready README.md** you can copy-paste directly.
It includes emojis, badges, tables, and clean structure.

---

# 🌟 **House Price Prediction — ML Model + REST API**

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.12-blue" />
  <img src="https://img.shields.io/badge/TensorFlow-2.x-orange" />
  <img src="https://img.shields.io/badge/Flask-API-green" />
  <img src="https://img.shields.io/badge/Status-Working-brightgreen" />
</p>

A complete machine learning project that trains a **house price prediction model** using TensorFlow and exposes it through a **REST API** built using Flask.
This project includes:

* Full model training pipeline
* Feature engineering (scaling + one-hot encoding)
* Saved model + scaler + column mapping
* Production-ready prediction API
* Ready for deployment on Render / AWS / Railway

---

# 📂 **Project Structure**

```
house_prediction_api/
│
├── model_training/
│   ├── train_model.py          # Training script
│   ├── Housing.csv             # Dataset
│   ├── house_model.h5          # Trained model
│   ├── scaler.pkl              # StandardScaler object
│   └── columns.pkl             # Encoded column names
│
├── api/
│   ├── app.py                  # Flask server
│   ├── house_model.h5          # Copied model
│   ├── scaler.pkl              # Copied scaler
│   ├── columns.pkl             # Copied columns
│   └── requirements.txt        # Dependencies
│
└── README.md
```

---

# 🚀 **Features**

### ✔ Fully working ML pipeline

### ✔ Neural network regression model

### ✔ One-hot encoding for categorical features

### ✔ StandardScaler for numerical features

### ✔ Saved + reloadable model components

### ✔ JSON-based prediction API

### ✔ Deployment-ready structure

---

# 🧠 **Model Training**

### 🔧 Step 1 — Move into the training folder

```bash
cd model_training
```

### 🔧 Step 2 — Run the training script

```bash
py train_model.py
```

This will:

| Output File        | Purpose                             |
| ------------------ | ----------------------------------- |
| **house_model.h5** | Trained TensorFlow model            |
| **scaler.pkl**     | Fitted StandardScaler               |
| **columns.pkl**    | Feature column order after encoding |

Copy these three files into the **api/** folder.

---

# 🌐 **Running the API Locally**

### 📥 Install dependencies:

```bash
cd api
py -m pip install -r requirements.txt
```

### ▶ Start the API:

```bash
py app.py
```

Server will run at:

```
http://127.0.0.1:5000/
```

---

# 🔥 **API Endpoint**

## **POST /predict**

### 📌 URL

`http://127.0.0.1:5000/predict`

### 📌 Request Body (JSON)

```json
{
  "area": 2000,
  "bedrooms": 3,
  "bathrooms": 2,
  "stories": 2,
  "mainroad": "yes",
  "guestroom": "no",
  "basement": "yes",
  "hotwaterheating": "no",
  "airconditioning": "yes",
  "parking": 1,
  "prefarea": "yes",
  "furnishingstatus": "furnished"
}
```

### 📌 Response Example

```json
{
  "predicted_price": 4893120.50
}
```

---

# 🛠 **Deployment Options**

You can deploy this API to:

### 🚀 **Render** (easiest)

### ☁️ **AWS EC2 / Lightsail**

### 🐳 **Docker Container**

### 🚂 **Railway.app**

### 🌐 **Heroku**

If you want, I can create a **Render deploy.yaml**, **Dockerfile**, or **AWS deployment guide**.

---

# 📦 **Requirements**

* Python 3.8+
* TensorFlow 2.x
* Flask
* pandas, numpy
* scikit-learn

All required packages for the API are already listed in:

```
api/requirements.txt
```

---

# 👩‍💻 **Author**

**Nisha G**
Machine Learning Developer
House Price Prediction Project

---

# ⭐ Want enhancements?

