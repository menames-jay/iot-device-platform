# Day 2 – Simulated Sensor

## 🎯 Goal

To implement a faux sensor with simulated parameters like temperature and humidity.

---

## 📚 Concepts Learned

### 1. Sensors in IoT

Sensors are essential devices in IoT. These make up the majority of the perception layer, which generate data from their surroundings.

### 2. Using JSON

The usage of JSON in writing a Python file for reading sensor data boils down to the fact that JSON is in a more human-readable format with its data in key-value pairs, as opposed to plain code.

---

## 🛠 What I Built

A Python MQTT client that:

* connects to the broker
* simulates sensor data, e.g. temperature and humidity
* publishes message in JSON format

---

## 🧾 Code Snippet

```python
    payload = generate_sensor_data()
    client.publish(TOPIC, json.dumps(payload))
    print("📤 Published: ", payload)
    time.sleep(5)
```

The variable 'payload' invokes the generate_sensor_data function which is used to simulate sensor data. The client publishes the payload in JSON format and rests for 5 seconds between each iteration.

---

## 🔍 Observations

* Publisher works as intended when ran.
* Sensor parameter values are generated at random within the range provided in the code.

---

## 📤 Output

Terminal output or behavior observed.

```
client = mqtt.Client()
📤 Published:  {'device_id': 'device1', 'timestamp': '2026-03-12T06:25:51.543509', 'temperature': 22.51, 'humidity': 77.88}
📤 Published:  {'device_id': 'device1', 'timestamp': '2026-03-12T06:25:56.544680', 'temperature': 31.02, 'humidity': 31.1}
📤 Published:  {'device_id': 'device1', 'timestamp': '2026-03-12T06:26:01.545505', 'temperature': 27.99, 'humidity': 77.92}
```

---

## 🧠 Key Takeaways

* IoT systems use sensors to generate and ingest data.
* The health and output of these sensors must be regularly monitored for efficient IoT systems.

---

## ⏭ Next Step

Developing auto-reconnecting logic when broker connection fails.