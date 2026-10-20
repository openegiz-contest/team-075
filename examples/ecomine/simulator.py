
import random
import time
from datetime import datetime

# EcoMine — экологиялық ақылды карьер
# Карьердегі өндіріс және экология симуляторы

MINE_NAME = "EcoMine Smart Open Pit"

# Карьердегі техникалар
trucks = [
    {"id": "TRUCK-01", "type": "electric", "capacity": 90},
    {"id": "TRUCK-02", "type": "electric", "capacity": 90},
    {"id": "TRUCK-03", "type": "diesel", "capacity": 110},
    {"id": "TRUCK-04", "type": "diesel", "capacity": 110},
]

# Экологиялық көрсеткіштер
total_ore = 0
total_energy = 0
total_water = 0
total_co2 = 0


def simulate_truck(truck):
    # Бір рейстегі тасымалданған кен
    ore = random.randint(50, truck["capacity"])

    if truck["type"] == "electric":
        energy = round(ore * 1.5, 2)
        co2 = round(energy * 0.25, 2)
    else:
        energy = round(ore * 3.0, 2)
        co2 = round(ore * 2.5, 2)

    water = round(ore * 0.4, 2)

    return ore, energy, water, co2


print("=" * 55)
print("       ECOMINE DIGITAL TWIN SIMULATOR")
print("=" * 55)
print("Mine:", MINE_NAME)
print("Trucks:", len(trucks))
print("Simulation started...")
print()

try:
    while True:
        for truck in trucks:
            ore, energy, water, co2 = simulate_truck(truck)

            total_ore += ore
            total_energy += energy
            total_water += water
            total_co2 += co2

            print(
                datetime.now().strftime("%H:%M:%S"),
                truck["id"],
                "| Ore:", ore, "t",
                "| Energy:", energy, "kWh-eq",
                "| Water:", water, "m3",
                "| CO2:", co2, "kg"
            )

        print("-" * 55)
        print("TOTAL ORE:", total_ore, "tonnes")
        print("TOTAL ENERGY:", round(total_energy, 2), "kWh-eq")
        print("TOTAL WATER:", round(total_water, 2), "m3")
        print("TOTAL CO2:", round(total_co2, 2), "kg")
        print("-" * 55)
        print()

        time.sleep(5)

except KeyboardInterrupt:
    print("\nEcoMine simulation stopped.")
