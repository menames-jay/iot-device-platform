import paho.mqtt.client as mqtt

BROKER = "localhost"
PORT = 1883
TOPIC = "iot/device1/#"

def on_message(client, userdata, msg):
    print(f"📥 Received: {msg.topic} -> {msg.payload.decode()}")

client = mqtt.Client()
client.on_message = on_message
client.connect(BROKER, PORT, 60)

client.subscribe(TOPIC)
print("👂 Listening for messages...")
client.loop_forever()