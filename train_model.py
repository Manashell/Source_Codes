import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import joblib

# Load the updated dataset
data = pd.read_csv("crop_data.csv")  # Ensure this includes both crops & vegetables

# Features & Target
X = data[["temperature", "humidity", "ph", "rainfall"]]
y = data["crop"]

# Encode labels into numbers
from sklearn.preprocessing import LabelEncoder
label_encoder = LabelEncoder()
y = label_encoder.fit_transform(y)

# Save the encoder for future use
joblib.dump(label_encoder, "label_encoder.pkl")

# Split Data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train Model
model = RandomForestClassifier(n_estimators=100)
model.fit(X_train, y_train)

# Save Model as crop_model.pkl
joblib.dump(model, "crop_model.pkl")

print("✅ Model trained and saved as 'crop_model.pkl'")
