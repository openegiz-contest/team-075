import json
import os
import urllib.request

import paho.mqtt.client as mqtt

INFLUX_URL = "http://localhost:8086"
INFLUX_TOKEN = os.environ["INFLUXDB_TOKEN"]
MQTT_TOPIC = "ecomine/telemetry"


def analyze_risk(co2):
    if co2 >= 200:
        return "CRITICAL", 2
    elif co2 >= 150:
        return "WARNING", 1
    return "NORMAL", 0


def save_risk(data):
    truck_id = data["truck_id"]
    co2 = float(data["co2_kg"])

    risk, level = analyze_risk(co2)

    line = (
        f"ecomine_risk,truck_id={truck_id},risk={risk} "
        f"co2_kg={co2},risk_level={level}i"
    )

    url = (
        f"{INFLUX_URL}/api/v2/write"
        "?org=opentwins&bucket=default&precision=ns"
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
        print(
            f"{truck_id} | CO2: {co2:.2f} kg | "
            f"RISK: {risk} | SAVED: {response.status}"
        )


def on_connect(client, userdata, flags, reason_code, properties):
    if reason_code == 0:
        client.subscribe(MQTT_TOPIC)
        print("EcoMine Risk Writer іске қосылды!")
    else:
        print("MQTT ERROR:", reason_code)


def on_message(client, userdata, message):
    try:
        data = json.loads(message.payload.decode())
        save_risk(data)
    except Exception as error:
        print("ERROR:", error)


client = mqtt.Client(
    callback_api_version=mqtt.CallbackAPIVersion.VERSION2
)

client.on_connect = on_connect
client.on_message = on_message

client.connect("localhost", 1883, 60)

try:
    client.loop_forever()
except KeyboardInterrupt:
    print("\nRisk Writer stopped.")
finally:
    client.disconnect()
