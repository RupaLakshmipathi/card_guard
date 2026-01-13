from flask import Flask, render_template, request
import pickle
import numpy as np
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

app = Flask(
    __name__,
    template_folder=os.path.join(BASE_DIR, "../frontend/templates"),
    static_folder=os.path.join(BASE_DIR, "../frontend/static")
)

# Load trained model
with open("fraud_model.pkl", "rb") as f:
    model = pickle.load(f)

@app.route("/", methods=["GET", "POST"])
def index():
    prediction = None
    risk_score = None
    risk_level = None

    if request.method == "POST":
        amount = float(request.form["amount"])
        time = float(request.form["time"])

        # Dummy PCA features for demo
        features = np.zeros(28)

        input_data = np.array([time] + list(features) + [amount]).reshape(1, -1)

        prob = model.predict_proba(input_data)[0][1] * 100
        risk_score = round(prob, 2)

        if risk_score > 75:
            risk_level = "HIGH RISK"
            prediction = "🚨 Fraudulent Transaction"
        elif risk_score > 40:
            risk_level = "MEDIUM RISK"
            prediction = "⚠️ Suspicious Transaction"
        else:
            risk_level = "LOW RISK"
            prediction = "✅ Legitimate Transaction"

    return render_template(
        "index.html",
        prediction=prediction,
        risk_score=risk_score,
        risk_level=risk_level
    )

if __name__ == "__main__":
    app.run(debug=True)
