import pandas as pd
import random
from datetime import datetime, timedelta


# Number of simulated records
TOTAL_RECORDS = 500

records = []

start_time = datetime.now() - timedelta(days=7)


for i in range(TOTAL_RECORDS):

    timestamp = start_time + timedelta(minutes=i * 20)

    # 80% Normal, 20% Unusual
    if random.random() < 0.80:

        # Normal simulated pattern
        urine_volume = random.randint(150, 450)
        ph = round(random.uniform(5.0, 7.5), 2)
        temperature = round(random.uniform(36.0, 37.0), 1)
        frequency = random.randint(4, 8)

        status = "Normal"

    else:

        # Unusual simulated pattern
        unusual_type = random.choice([
            "low_volume",
            "high_volume",
            "low_ph",
            "high_ph",
            "high_frequency"
        ])

        # Start with normal values
        urine_volume = random.randint(150, 450)
        ph = round(random.uniform(5.0, 7.5), 2)
        temperature = round(random.uniform(36.0, 37.0), 1)
        frequency = random.randint(4, 8)

        # Create one simulated unusual pattern
        if unusual_type == "low_volume":
            urine_volume = random.randint(50, 149)

        elif unusual_type == "high_volume":
            urine_volume = random.randint(451, 700)

        elif unusual_type == "low_ph":
            ph = round(random.uniform(4.6, 4.99), 2)

        elif unusual_type == "high_ph":
            ph = round(random.uniform(7.51, 8.0), 2)

        elif unusual_type == "high_frequency":
            frequency = random.randint(9, 15)

        status = "Unusual"


    records.append({
        "timestamp": timestamp.strftime("%Y-%m-%d %H:%M:%S"),
        "urine_volume_ml": urine_volume,
        "ph": ph,
        "temperature_c": temperature,
        "frequency_per_day": frequency,
        "status": status
    })


# Create DataFrame
df = pd.DataFrame(records)


# Shuffle the dataset
df = df.sample(frac=1, random_state=42).reset_index(drop=True)


# Save dataset
output_file = "data/ml_dataset.csv"

df.to_csv(output_file, index=False)


# Display results
print("Improved ML dataset created successfully!")
print(f"Total records: {len(df)}")

print("\nStatus distribution:")
print(df["status"].value_counts())

print(f"\nDataset saved to: {output_file}")