import paho.mqtt.client as mqtt
import time

BROKER = "localhost"
PORT = 1883
TOPIC = "iot/device1/test"

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("✅ Connected to MQTT Broker!")
    else:
        print("❌ Connection failed")

client = mqtt.Client()
client.on_connect = on_connect
client.connect(BROKER, PORT, 60)
client.loop_start()

count = 0

while True:
    message = f"Hello MQTT! Count: {count}"
    client.publish(TOPIC, message)
    print(f"📤 Published: {message}")

    count += 1
    time.sleep(3)