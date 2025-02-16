from flask import Flask, render_template, request, jsonify
import joblib
import numpy as np

app = Flask(__name__)

# Load trained model & label encoder
model = joblib.load("crop_model.pkl")
label_encoder = joblib.load("label_encoder.pkl")

@app.route("/")
def home():
    return render_template("main.html")

@app.route("/predict", methods=["POST"])
def predict():
    try:
        data = request.get_json()

        # Extract input values safely
        temperature = float(data.get("temperature", 0))
        humidity = float(data.get("humidity", 0))
        ph = float(data.get("ph", 0))
        rainfall = float(data.get("rainfall", 0))

        features = np.array([[temperature, humidity, ph, rainfall]])
        prediction = model.predict(features)[0]

        # Convert numeric prediction to crop/vegetable name
        crop_name = label_encoder.inverse_transform([prediction])[0]

        return jsonify({"crop": crop_name})  # ✅ Now returns grains or vegetables

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
