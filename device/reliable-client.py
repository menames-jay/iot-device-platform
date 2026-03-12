import paho.mqtt.client as mqtt
import time
import json
import random

BROKER = "localhost"
PORT = 1883
TOPIC = "iot/device1/telemetry"

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("✅Connected to MQTT Broker!")
    else:
        print("❌ Connection failed")

def on_disconnect(client, userdata, rc):
    print("⚠️ Disconnected from MQTT Broker")

client = mqtt.Client()
client.on_connect = on_connect
client.on_disconnect = on_disconnect

client.reconnect_delay_set(min_delay=1, max_delay=120)

client.connect(BROKER, PORT)
client.loop_start()

while True:
    data = {
        "temperature": round(random.uniform(20, 35), 2),
        "humidity": round(random.uniform(40, 70), 2)
    }
    
    result = client.publish(TOPIC, json.dumps(data))
    
    if result.rc == mqtt.MQTT_ERR_SUCCESS:
        print("📤 Published:", data)
    else:
        print("❌ Failed to publish message")
    
    time.sleep(5)
