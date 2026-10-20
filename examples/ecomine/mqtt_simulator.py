import os

import json
import random
import time
from datetime import datetime

import paho.mqtt.client as mqtt

# EcoMine MQTT параметрлері
BROKER = os.getenv("MQTT_HOST", "localhost")
PORT = 1883
TOPIC = "ecomine/telemetry"

# Карьердегі самосвалдар
trucks = [
    {"id": "TRUCK-01", "type": "electric"},
    {"id": "TRUCK-02", "type": "electric"},
    {"id": "TRUCK-03", "type": "diesel"},
    {"id": "TRUCK-04", "type": "diesel"},
]

client = mqtt.Client(
    callback_api_version=mqtt.CallbackAPIVersion.VERSION2
)

client.connect(BROKER, PORT, 60)
client.loop_start()

print("EcoMine MQTT simulator started!")

try:
    while True:
        for truck in trucks:
            ore = random.randint(50, 100)

            if truck["type"] == "electric":
                energy = ore * 1.5
                co2 = energy * 0.25
            else:
                energy = ore * 3.0
                co2 = ore * 2.5

            data = {
                "mine": "EcoMine",
                "truck_id": truck["id"],
                "truck_type": truck["type"],
                "ore_tonnes": ore,
                "energy_kwh_equivalent": round(energy, 2),
                "water_m3": round(ore * 0.4, 2),
                "co2_kg": round(co2, 2),
                "timestamp": datetime.now().isoformat()
            }

            message = json.dumps(data)

            result = client.publish(TOPIC, message, qos=1)
            result.wait_for_publish()

            print("SENT:", message)

        print("-" * 50)
        time.sleep(5)

except KeyboardInterrupt:
    print("\nEcoMine simulator stopped.")

finally:
    client.disconnect()
    client.loop_stop()
