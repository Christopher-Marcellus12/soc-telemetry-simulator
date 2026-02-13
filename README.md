# 🛡️ Wazuh SOC Telemetry Simulator

![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)
![Python](https://img.shields.io/badge/Python-3.x-blue)
![Docker](https://img.shields.io/badge/Docker-Containerized-2496ED?logo=docker&logoColor=white)
![Wazuh](https://img.shields.io/badge/SIEM-Wazuh-green)
![Security](https://img.shields.io/badge/Cybersecurity-SOC%20Lab-red)
![Status](https://img.shields.io/badge/Project-Active-success)

A Dockerized SOC lab using **Wazuh SIEM** and a custom Python telemetry generator that emits realistic security events like:

- SSH brute force
- Network scanning
- Privilege escalation
- Suspicious commands

Built for threat hunting practice and blue-team portfolio demonstrations.

# soc-telemetry-simulator

A Dockerized SOC lab using **Wazuh SIEM** plus a custom **Python telemetry generator** that emits realistic security events (SSH brute force, scanning, privilege escalation, suspicious commands) for **threat hunting practice**.

## What this demonstrates
- SIEM deployment (Wazuh Manager + Indexer + Dashboard)
- Security telemetry generation (simulated attacks, safe)
- Log ingestion + dashboards for SOC workflows
- Threat hunting practice aligned with Security+ concepts

## Architecture
Telemetry Generator → Wazuh Manager → Indexer (OpenSearch) → Wazuh Dashboard

## Requirements
- Docker Desktop (Apple Silicon M2 supported)
- Git

## Quick Start
```bash
cd single-node

# Generate certs (if your folder includes the generator file)
docker compose -f generate-indexer-certs.yml run --rm generator

# Start Wazuh stack
docker compose up -d

# Start the telemetry generator
docker compose up -d telemetry-generator
