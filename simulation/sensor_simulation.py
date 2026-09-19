import random
import time
import csv
import os
from datetime import datetime


# CSV file location
csv_file = "data/sensor_data.csv"


def generate_sensor_data():
    # Simulated urine volume per visit
    urine_volume = random.randint(200, 450)

    # Medically referenced urine pH range
    ph = round(random.uniform(4.6, 8.0), 2)

    # Simulated urine temperature
    temperature = round(random.uniform(35.5, 37.0), 1)

    # Simulated daily frequency
    frequency = random.randint(4, 8)

    return {
        "urine_volume_ml": urine_volume,
        "ph": ph,
        "temperature_c": temperature,
        "frequency_per_day": frequency
    }


# Create CSV file with column names if it doesn't exist
if not os.path.exists(csv_file):
    with open(csv_file, "w", newline="") as file:
        writer = csv.writer(file)

        writer.writerow([
            "timestamp",
            "urine_volume_ml",
            "ph",
            "temperature_c",
            "frequency_per_day"
        ])


# Generate sensor data continuously
while True:

    data = generate_sensor_data()

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Save data to CSV
    with open(csv_file, "a", newline="") as file:
        writer = csv.writer(file)

        writer.writerow([
            timestamp,
            data["urine_volume_ml"],
            data["ph"],
            data["temperature_c"],
            data["frequency_per_day"]
        ])

    # Display data in terminal
    print("\n--- Smart AI Health Monitoring Toilet ---")
    print(f"Time           : {timestamp}")
    print(f"Urine Volume   : {data['urine_volume_ml']} ml")
    print(f"pH             : {data['ph']}")
    print(f"Temperature    : {data['temperature_c']} °C")
    print(f"Frequency      : {data['frequency_per_day']} times/day")

    time.sleep(3)