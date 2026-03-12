# Day 3 – Reliability Basics

## 🎯 Goal

To implement automatic reconnect logic for MQTT devices.

---

## 📚 Concepts Learned

### 1. Importance of Reliability

Reliability is an important factor in designing an IoT system since a system needs to prepare for failures such as disconnecting from broker.

### 2. Disconnected System Behaviour

A system disconnected from its MQTT broker cannot publish any messages or topics.

---

## 🛠 What I Built

A Python MQTT client that:

* connects to the broker
* publishes telemetry
* automatically reconnects if disconnected

---

## 🧾 Code Snippet

```python
client.reconnect_delay_set(min_delay=1, max_delay=120)
```

This line of code attempts to reconnect with the MQTT client or broker after a set amount of time.

---

## 🔍 Observations

* MQTT broker publishes sensor data when connected.
* System does not publish any data when disconnected.

---

## 📤 Output

Terminal output or behavior observed.

Connected Output
```
✅Connected to MQTT Broker!
📤 Published: {'temperature': 29.02, 'humidity': 60.25}
📤 Published: {'temperature': 21.78, 'humidity': 47.7}
📤 Published: {'temperature': 34.69, 'humidity': 44.76}
```

Disconnected Output
```
⚠️ Disconnected from MQTT Broker
❌ Failed to publish message
❌ Failed to publish message
```

---

## 🧠 Key Takeaways

* IoT systems must assume unreliable networks.
* Devices should reconnect automatically.

---

## ⏭ Next Step

To test QoS delivery guarantees and duplicate handling.
