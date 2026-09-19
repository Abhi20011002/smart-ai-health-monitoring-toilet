import paho.mqtt.client as mqtt
import csv
import os
from datetime import datetime

BROKER = "broker.emqx.io"
PORT = 1883
TOPIC = "smart-toilet/abhi2026/liveph"
CSV_FILE = "data/sensor_data.csv"


def on_connect(client, userdata, flags, reason_code, properties):
    print("MQTT Connected:", reason_code)

    result, mid = client.subscribe(TOPIC, qos=1)

    if result == mqtt.MQTT_ERR_SUCCESS:
        print("Subscribed successfully:", TOPIC)
    else:
        print("Subscribe failed:", result)


def on_message(client, userdata, msg):
    try:
        ph = float(msg.payload.decode())

        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        # Baaki sensors abhi simulated hain
        urine_volume = 300
        temperature = 36.5
        frequency = 6

        file_exists = os.path.exists(CSV_FILE)

        with open(CSV_FILE, "a", newline="") as file:
            writer = csv.writer(file)

            if not file_exists:
                writer.writerow([
                    "timestamp",
                    "urine_volume_ml",
                    "ph",
                    "temperature_c",
                    "frequency_per_day"
                ])

            writer.writerow([
                timestamp,
                urine_volume,
                ph,
                temperature,
                frequency
            ])

        print(f"Received pH: {ph:.2f}")
        print(f"Saved to CSV: {CSV_FILE}")

    except Exception as e:
        print("Error:", e)


client = mqtt.Client(
    callback_api_version=mqtt.CallbackAPIVersion.VERSION2
)

client.on_connect = on_connect
client.on_message = on_message

print("Connecting to MQTT broker...")

client.connect(BROKER, PORT, 60)

client.loop_forever()