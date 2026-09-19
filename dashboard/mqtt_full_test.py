import paho.mqtt.client as mqtt
import time

BROKER = "broker.emqx.io"
PORT = 1883
TOPIC = "smart-toilet/abhi2026/test"

def on_connect(client, userdata, flags, reason_code, properties):
    print("Connected:", reason_code)
    client.subscribe(TOPIC)
    print("Subscribed:", TOPIC)

def on_message(client, userdata, msg):
    print("MESSAGE RECEIVED:", msg.payload.decode())

client = mqtt.Client(
    callback_api_version=mqtt.CallbackAPIVersion.VERSION2
)

client.on_connect = on_connect
client.on_message = on_message

print("Connecting...")
client.connect(BROKER, PORT, 60)

client.loop_start()

time.sleep(2)

print("Publishing test message...")
client.publish(TOPIC, "HELLO_123", qos=1)

time.sleep(5)

client.loop_stop()
client.disconnect()

print("Test finished!")