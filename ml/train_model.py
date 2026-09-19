import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
import joblib


# Load ML dataset
data = pd.read_csv("data/ml_dataset.csv")


# Features used by the ML model
features = [
    "urine_volume_ml",
    "ph",
    "temperature_c",
    "frequency_per_day"
]

X = data[features]
y = data["status"]


# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42,
    stratify=y
)


# Create Random Forest model
model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)


# Train the model
model.fit(X_train, y_train)


# Make predictions
y_pred = model.predict(X_test)


# Calculate accuracy
accuracy = accuracy_score(y_test, y_pred)

print("\n--- Smart AI Health Monitoring Toilet ---")
print("ML Model Training Completed!")

print(f"\nTraining records: {len(X_train)}")
print(f"Testing records : {len(X_test)}")
print(f"Accuracy        : {accuracy * 100:.2f}%")


print("\nClassification Report:")
print(classification_report(y_test, y_pred))


# Save trained model
model_file = "ml/health_monitoring_model.pkl"

joblib.dump(model, model_file)

print(f"Model saved to: {model_file}")