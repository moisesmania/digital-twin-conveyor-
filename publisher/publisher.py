import json
import random
import time
import paho.mqtt.client as mqtt

BROKER = "mosquitto"
TOPIC = "conveyor/data"

def generate_payload():
    return {
        "beltSpeed": round(random.uniform(2.0, 3.0), 2),
        "motorCurrent": round(random.uniform(80, 120), 2),
        "vibration": round(random.uniform(2, 5), 2),
        "load": round(random.uniform(60, 95), 2),
        "status": "OK",
        "lossPerHour": round(random.uniform(0, 10), 2)
    }

client = mqtt.Client()
client.connect(BROKER, 1883, 60)
client.loop_start()

while True:
    payload = generate_payload()

    result = client.publish(TOPIC, json.dumps(payload))

    print("PUBLISHED:", payload, "RESULT:", result.rc)

    time.sleep(5)