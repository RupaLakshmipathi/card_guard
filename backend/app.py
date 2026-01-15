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
model_path = os.path.join(BASE_DIR, "fraud_model.pkl")
with open(model_path, "rb") as f:
    model = pickle.load(f)

@app.route("/", methods=["GET", "POST"])
def index():
    prediction = None

    if request.method == "POST":
        amount = float(request.form["amount"])
        time = float(request.form["time"])

        # Rule-based high risk detection (REALISTIC)
        if amount > 50000 and (time < 6 or time > 22):
            prediction = "🚨 High Risk Fraudulent Transaction"
        else:
            # Model prediction fallback
            features = np.zeros(28)
            input_data = np.array([time] + list(features) + [amount]).reshape(1, -1)
            result = model.predict(input_data)[0]

            prediction = (
                "🚨 Fraudulent Transaction"
                if result == 1
                else "✅ Legitimate Transaction"
            )

    return render_template("index.html", prediction=prediction)

if __name__ == "__main__":
    app.run(debug=True)
