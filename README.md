💳 CardGuard – Credit Card Fraud Detection System
📌 System

CardGuard is a machine learning–based fraud detection system designed to identify suspicious and unauthorized credit card transactions in real time.
The system analyzes transaction patterns using statistical features and ML models to minimize financial loss and enhance transaction security.

🚀 Features

🔍 Real-time fraud detection

🤖 ML-based transaction classification

⚖️ Class imbalance handling

📊 Exploratory Data Analysis (EDA)

📈 Transaction risk prediction

🌐 User-friendly and interactive web interface

🔐 High accuracy fraud identification

🧠 AI & ML

Logistic Regression

Random Forest Classifier

Feature Scaling (StandardScaler)

Class Imbalance Handling (class_weight = balanced)

Model Evaluation using Precision, Recall & F1-score

Pipeline-based ML architecture

🛠️ Tech Stack
Frontend

HTML

CSS

JavaScript

Backend

Python

Flask

Machine Learning

scikit-learn

pandas

NumPy

📁 Project Structure
card_guard/
│
├── backend/
│   ├── app.py
│   ├── train_model.py
│   ├── fraud_model.pkl
│   ├── scaler.pkl
│
├── templates/
│   └── index.html
│
├── static/
│   ├── style.css
│   └── script.js
│
├── dataset/
│   └── creditcard.csv
│
├── requirements.txt
└── README.md

⚙️ How It Works

User enters transaction details (amount, time, etc.).

Input data is scaled and preprocessed.

ML model evaluates transaction patterns.

System predicts Fraud or Legitimate.

Result is displayed instantly on the UI.

📊 Model Workflow

Data Cleaning & Preprocessing

Feature Scaling

Handling Class Imbalance

Model Training & Evaluation

Model Serialization (.pkl)

Real-time Prediction using Flask

🎯 Use Cases

Banking & Financial Institutions

Online Payment Gateways

Credit Card Transaction Monitoring

Academic & Hackathon Projects

🔮 Future Enhancements

📉 Deep Learning-based fraud detection

📊 Advanced fraud analytics dashboard

⏱️ Time-series anomaly detection

🔔 Real-time alerts & notifications

☁️Cloud deployment
