import paho.mqtt.publish as publish

publish.single(
    "smart-toilet/abhi2026/ph",
    "6.55",
    hostname="broker.emqx.io",
    port=1883,
    qos=1,
    retain=True
)

print("Test message sent!")