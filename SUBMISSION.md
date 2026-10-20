# EcoMine — Intelligent Green Mining Digital Twin

**Team:** 075
**Platform:** OpenEgiz v1.0.4
**Repository:** https://github.com/openegiz-contest/team-075

## Project Overview

EcoMine is an environmental monitoring and digital twin prototype for mining operations.

The system simulates mining truck telemetry, processes environmental measurements, stores time-series data, updates a digital twin, and visualizes operational indicators through Grafana.

The main goal is to demonstrate how mining enterprises can monitor environmental performance and identify potentially high-emission operating conditions.

## Mine Model and Digital Twin

The prototype represents a simulated open-pit mining haulage operation with four trucks.

Each truck generates telemetry containing:
- Truck identifier and type
- Ore transported, in tonnes
- Energy consumption equivalent, in kWh
- Water consumption, in cubic metres
- CO2 emissions, in kilograms
- Timestamp

The Eclipse Ditto digital twin is represented by the Thing ID:

`ecomine:smart-mine`

The twin is updated through the Ditto HTTP API.

Implementation:
- `examples/ecomine/mqtt_simulator.py`
- `examples/ecomine/ditto_bridge.py`

## Architecture

Data flow:

Mining Truck Simulator
→ MQTT / Mosquitto
→ InfluxDB Writers
→ InfluxDB
→ Grafana Dashboard and Risk Alert

In parallel:

MQTT / Mosquitto
→ Ditto Bridge
→ Eclipse Ditto Digital Twin

Technologies:
- Python
- Docker Compose
- MQTT / Eclipse Mosquitto
- InfluxDB
- Eclipse Ditto
- Grafana

## Modules and What-if Scenarios

| Module or What-if Scenario | What it does | How to see it on the Stand | How to undo it (scenarios) |
|---|---|---|---|
| Truck Telemetry Simulation | Generates synthetic telemetry for four mining trucks | MQTT telemetry and Grafana | Stop the simulator container |
| Environmental Monitoring | Records CO2, water, energy and ore measurements | Grafana dashboard | Not applicable |
| Environmental Risk Analysis | Classifies simulated CO2 measurements as NORMAL, WARNING or CRITICAL | Environmental Risk panel and service logs | Not applicable |
| Digital Twin Synchronization | Updates the EcoMine Thing in Eclipse Ditto | Ditto HTTP API | Not applicable |
| Critical Risk Alert | Detects critical risk values using a Grafana alert rule | Grafana Alerting | Not applicable |

No interactive what-if scenario has been verified. The current prototype demonstrates continuous telemetry processing and risk monitoring.

## What Works and What Does Not

Verified locally:
- Four EcoMine Docker services start successfully.
- MQTT telemetry is generated.
- InfluxDB accepts telemetry and risk measurements (HTTP 204).
- Eclipse Ditto accepts digital twin updates (HTTP 204).
- Five Grafana panels display environmental and operational measurements.
- A Grafana critical-risk alert has been observed in FIRING state.

Not yet verified:
- Fresh installation on a separate computer.
- Automatic provisioning of the Grafana dashboard and alert on a clean deployment.
- Interactive operational what-if scenarios.

## Data and Assumptions

All mining telemetry is synthetic.

The prototype does not use confidential enterprise data or personal data.

The risk classification is a demonstration rule based on CO2 mass per simulated telemetry record:

- NORMAL: CO2 below 150 kg
- WARNING: CO2 from 150 kg to below 200 kg
- CRITICAL: CO2 of 200 kg or above

These thresholds are prototype assumptions, not regulatory or industrial safety limits.

The data is intended for software demonstration and does not represent validated measurements from a real mine.

## Mine Visualization

Grafana dashboard:

`http://localhost:3000`

The dashboard includes:
1. CO2 Emissions
2. Water Consumption
3. Energy Consumption
4. Ore Transportation
5. Environmental Risk

The Grafana alerting interface displays the critical environmental risk alert.

These are local development addresses. External Stand URLs have not yet been verified.

## Limitations

- The system currently uses simulated truck data.
- No physical mining equipment is connected.
- Risk thresholds are illustrative.
- The digital twin represents aggregated mining telemetry rather than a fully modeled industrial mine.
- Dashboard and alert provisioning require further automation.
- No interactive what-if scenario is currently implemented.

## Presentation

`presentation.pdf` will be added to the repository root.

---

Platform: OpenEgiz v1.0.4.
