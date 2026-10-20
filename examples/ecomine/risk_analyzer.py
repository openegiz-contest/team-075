import json
import paho.mqtt.client as mqtt

BROKER = "localhost"
TOPIC = "ecomine/telemetry"

def analyze(co2):
    if co2 >= 200:
        return "CRITICAL"
    elif co2 >= 150:
        return "WARNING"
    return "NORMAL"

def on_connect(client, userdata, flags, reason_code, properties):
    client.subscribe(TOPIC)
    print("EcoMine Risk Analyzer іске қосылды!")

def on_message(client, userdata, message):
    data = json.loads(message.payload.decode())

    truck = data.get("truck_id", "UNKNOWN")
    co2 = float(data.get("co2_kg", 0))
    risk = analyze(co2)

    print(f"{truck} | CO2: {co2:.2f} kg | RISK: {risk}")

client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
client.on_connect = on_connect
client.on_message = on_message

client.connect(BROKER, 1883, 60)
client.loop_forever()
