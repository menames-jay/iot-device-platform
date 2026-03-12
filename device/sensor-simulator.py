import paho.mqtt.client as mqtt
import time
import json
import random
from datetime import datetime

BROKER = "localhost"
PORT = 1883
TOPIC = "iot/device1/telemetry"

client = mqtt.Client()
client.connect(BROKER, PORT, 60)
client.loop_start()

def generate_sensor_data():
    data = {
        "device_id": "device1",
        "timestamp": datetime.utcnow().isoformat(),
        "temperature": round(random.uniform(20, 35), 2),
        "humidity": round(random.uniform(30, 80), 2)
    }
    return data

while True:
    payload = generate_sensor_data()
    client.publish(TOPIC, json.dumps(payload))
    print("📤 Published: ", payload)
    time.sleep(5)
