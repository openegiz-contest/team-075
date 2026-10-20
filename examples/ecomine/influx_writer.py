
import json
import os
import urllib.request
import urllib.error

import paho.mqtt.client as mqtt

# InfluxDB баптаулары
INFLUX_URL = "http://localhost:8086"
INFLUX_TOKEN = os.environ["INFLUXDB_TOKEN"]
ORG = "opentwins"
BUCKET = "default"

MQTT_TOPIC = "ecomine/telemetry"


def save_to_influx(data):
    # InfluxDB Line Protocol форматы
    truck_id = data["truck_id"]
    truck_type = data["truck_type"]

    line = (
        f"ecomine,truck_id={truck_id},truck_type={truck_type} "
        f"ore_tonnes={float(data['ore_tonnes'])},"
        f"energy_kwh={float(data['energy_kwh_equivalent'])},"
        f"water_m3={float(data['water_m3'])},"
        f"co2_kg={float(data['co2_kg'])}"
    )

    url = (
        f"{INFLUX_URL}/api/v2/write"
        f"?org={ORG}&bucket={BUCKET}&precision=ns"
    )

    request = urllib.request.Request(
        url,
        data=line.encode(),
        headers={
            "Authorization": f"Token {INFLUX_TOKEN}",
            "Content-Type": "text/plain"
        },
        method="POST"
    )

    with urllib.request.urlopen(request, timeout=10) as response:
        print("INFLUX SAVED:", truck_id, response.status)


def on_connect(client, userdata, flags, reason_code, properties):
    if reason_code == 0:
        print("MQTT connected!")
        client.subscribe(MQTT_TOPIC)
    else:
        print("MQTT connection error:", reason_code)


def on_message(client, userdata, message):
    try:
        data = json.loads(message.payload.decode())
        save_to_influx(data)
    except Exception as error:
        print("ERROR:", error)


client = mqtt.Client(
    callback_api_version=mqtt.CallbackAPIVersion.VERSION2
)

client.on_connect = on_connect
client.on_message = on_message

print("EcoMine InfluxDB Writer started!")

client.connect("localhost", 1883, 60)

try:
    client.loop_forever()
except KeyboardInterrupt:
    print("\nEcoMine InfluxDB Writer stopped.")
finally:
    client.disconnect()
