# EcoMine — Intelligent Green Mining Digital Twin

**Team 075 | OpenEgiz v1.0.4**

EcoMine is a real-time environmental monitoring and digital twin prototype for a simulated open-pit mine.

## Key Features

- Four simulated mining trucks
- Real-time MQTT telemetry
- CO2 emissions monitoring
- Water and energy consumption analytics
- Environmental risk classification
- Eclipse Ditto digital twin
- InfluxDB time-series storage
- Five Grafana dashboard panels
- Critical environmental risk alerts
- Docker Compose deployment

## System Architecture

Mining Trucks -> MQTT -> InfluxDB -> Grafana

Mining Trucks -> MQTT -> Risk Analyzer -> InfluxDB

Mining Trucks -> MQTT -> Eclipse Ditto Digital Twin

## Technology Stack

| Technology | Purpose |
|---|---|
| Python | Telemetry simulation and processing |
| MQTT | Real-time data streaming |
| InfluxDB | Time-series storage |
| Grafana | Monitoring and alerts |
| Eclipse Ditto | Digital twin |
| Docker | Container deployment |

## Running EcoMine

First configure and start the OpenEgiz platform.

EcoMine services are defined in:

`deploy/compose/ecomine.yml`

A valid InfluxDB token must be provided through the
`ECOMINE_INFLUX_TOKEN` environment variable.

Run from the repository root:

`docker compose --env-file deploy/compose/.env -f deploy/compose/docker-compose.yml -f deploy/compose/ecomine.yml up -d --build`

## Local Interfaces

- Grafana: http://localhost:3000
- InfluxDB: http://localhost:8086
- Eclipse Ditto API: http://localhost:8080

## Current Limitations

- All mining telemetry is synthetic.
- Risk thresholds are illustrative.
- Grafana dashboard and alert provisioning are not yet automated.
- Fresh installation on another computer has not been verified.

For submission details, see `SUBMISSION.md`.

---

## Original OpenEgiz Documentation

# <Team name>: a digital mine on OpenEgiz

> Team Repository of the contest “Digital Mine on OpenEgiz”. **Replace the contents of this file with the instructions for your Submission.** The AI Jury runs the Submission strictly by these instructions, from scratch, in the Judge Environment. Accepted languages: English, Kazakh, Russian.

> **Start with the Concept**, the first section of [SUBMISSION.md](SUBMISSION.md): the Team writes it before any code. What AI agents build from this Template without a Concept is the Default Solution, published on the [contest site](https://openegiz-contest.github.io/) as the low bar: a Submission that does not go beyond it gets low levels in the Rubric. AI agents read [AGENTS.md](AGENTS.md).

## Running

Requirements (Docker, `make`, Windows/WSL2 setup) are in [OPENEGIZ.md](OPENEGIZ.md) / [OPENEGIZ.ru.md](OPENEGIZ.ru.md).

```bash
sudo apt install -y make   # if make is missing (clean Ubuntu)
make up            # the OpenEgiz platform
make example-mine  # the Example Mine: twins, simulator, dashboard
```

Replace these commands with the commands of your Submission. The Submission must start by following these instructions without manual intervention (Rules, clause 6.4); downloading datasets and models and building are also listed here.

## What to open

- Grafana: the address and login are printed by `make up`.
- <where to see the mine visualization, which dashboards>

## Repository contents

| Path | Contents |
|---|---|
| `team/` | Directory for the Team's code. Using it is optional: any part may be changed, including the platform core |
| `SUBMISSION.md` | Description of the Submission: **required** |
| `presentation.pdf` | Presentation: **required**, in the repository root |
| `AGENTS.md`, `CLAUDE.md` | Instructions for your AI agents (Codex, Claude Code and others read them automatically) |
| `examples/mine/` | The Example Mine: shows how a digital mine is built on OpenEgiz. It is not a basis for the Submission |
| `OPENEGIZ.md`, `OPENEGIZ.ru.md` | Documentation of the OpenEgiz platform v1.0.4 |

The Submission is the `main` branch at the moment of the Freeze; other branches are not evaluated.

## License

The Submission is distributed under the MIT license, see [LICENSE](LICENSE). Copyright belongs to the Team: add the line `Copyright (c) 2026 <Team members>` to `LICENSE`.

---

Platform: [aleka07/openegiz](https://github.com/aleka07/openegiz). If the platform was useful to you, support the project with a star on GitHub.
