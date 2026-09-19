import pandas as pd
import joblib


# Load trained ML model
model = joblib.load("ml/health_monitoring_model.pkl")


print("\n--- Smart AI Health Monitoring Toilet ---")
print("Enter sensor readings:\n")


# Get sensor values from user
urine_volume = float(input("Urine Volume (ml): "))
ph = float(input("Urine pH: "))
temperature = float(input("Temperature (°C): "))
frequency = int(input("Frequency (times/day): "))


# Create input data
new_data = pd.DataFrame([{
    "urine_volume_ml": urine_volume,
    "ph": ph,
    "temperature_c": temperature,
    "frequency_per_day": frequency
}])


# Make prediction
prediction = model.predict(new_data)[0]


print("\n-----------------------------")
print("AI Prediction:", prediction)
print("-----------------------------")


if prediction == "Normal":
    print("Pattern appears within the simulated normal range.")
else:
    print("Unusual pattern detected.")
    print("Further evaluation may be appropriate.")