
import json
import os
import urllib.request
import urllib.error
import base64

import paho.mqtt.client as mqtt

# EcoMine цифрлық егізінің мекенжайы
DITTO_URL = os.getenv("DITTO_URL", "http://localhost:8080/api/2/things/ecomine:smart-mine")

USERNAME = "ditto"
PASSWORD = os.environ["DITTO_PASSWORD"]

MQTT_BROKER = os.getenv("MQTT_HOST", "localhost")
MQTT_TOPIC = "ecomine/telemetry"

# Ditto авторизациясы
credentials = base64.b64encode(
    f"{USERNAME}:{PASSWORD}".encode()
).decode()


def update_ditto(data):
    # MQTT деректерін Ditto форматына айналдыру
    features = {
        "production": {
            "properties": {
                "ore_tonnes": data["ore_tonnes"]
            }
        },
        "environment": {
            "properties": {
                "co2_kg": data["co2_kg"],
                "water_m3": data["water_m3"],
                "energy_kwh_equivalent": data["energy_kwh_equivalent"]
            }
        },
        "transport": {
            "properties": {
                "last_truck_id": data["truck_id"],
                "last_truck_type": data["truck_type"],
                "electric_trucks": 2,
                "diesel_trucks": 2
            }
        }
    }

    request = urllib.request.Request(
        DITTO_URL + "/features",
        data=json.dumps(features).encode(),
        headers={
            "Content-Type": "application/json",
            "Authorization": "Basic " + credentials
        },
        method="PUT"
    )

    with urllib.request.urlopen(request, timeout=10) as response:
        print("DITTO UPDATED:", data["truck_id"], response.status)


def on_connect(client, userdata, flags, reason_code, properties):
    if reason_code == 0:
        print("MQTT connected!")
        client.subscribe(MQTT_TOPIC)
    else:
        print("MQTT connection failed:", reason_code)


def on_message(client, userdata, message):
    try:
        data = json.loads(message.payload.decode())
        update_ditto(data)
    except Exception as error:
        print("ERROR:", error)


client = mqtt.Client(
    callback_api_version=mqtt.CallbackAPIVersion.VERSION2
)

client.on_connect = on_connect
client.on_message = on_message

print("EcoMine Ditto Bridge starting...")

client.connect(MQTT_BROKER, 1883, 60)

try:
    client.loop_forever()
except KeyboardInterrupt:
    print("\nEcoMine Ditto Bridge stopped.")
finally:
    client.disconnect()
