# Day 1 – MQTT Basics

## 🎯 Goal

To learn essential MQTT basics such as publishing and subscribing.

---

## 📚 Concepts Learned

### 1. Concept Name

MQTT uses a **publish/subscribe model** where devices send messages to topics instead of direct connections.
Here, a single publisher can send messages to all its subscribed devices.

---

### 2. Concept Name

Publishers and subscribers are connected via brokers.
These brokers manage the messages that are sent to subscribers from the publishers.

---

## 🛠 What I Built

A Python MQTT client that:

* connects to the broker
* publishes a small message
* helps subscriber(s) receive and verify the message

---

## 🧾 Code Snippet

```python
while True:
    message = f"Hello MQTT! Count: {count}"
    client.publish(TOPIC, message)
    print(f"📤 Published: {message}")

    count += 1
    time.sleep(3)
```

This is a simple MQTT program that publishes a sample message within intervals of 3 seconds, and prints the published message.
To prove that this is indeed working as intended and not looping the same publish again and again, count variable has been set to increase every 3 seconds and publish the message again.

---

## 🔍 Observations


* Publisher works as intended when ran.
* Subscriber verifies the same by receiving the published topic.

---

## 📤 Output

Terminal output or behavior observed.


Publisher Terminal Output:
```
 client = mqtt.Client()
✅ Connected to MQTT Broker!
📤 Published: Hello MQTT! Count: 0
📤 Published: Hello MQTT! Count: 1
📤 Published: Hello MQTT! Count: 2
📤 Published: Hello MQTT! Count: 3
```


Subscriber Terminal Output:
```
  client = mqtt.Client()
👂 Listening for messages...
📥 Received: iot/device1/test -> Hello MQTT! Count: 0
📥 Received: iot/device1/test -> Hello MQTT! Count: 1
📥 Received: iot/device1/test -> Hello MQTT! Count: 2
📥 Received: iot/device1/test -> Hello MQTT! Count: 3
```

---

## 🧠 Key Takeaways


* IoT systems use MQTT for fast, simple and reliable communication.
* Devices are divided into publishers and subscribers, which communicate via brokers.

---

## ⏭ Next Step

Build a faux sensor with simulated parameters like temperature and humidity.

---
