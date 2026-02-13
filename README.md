![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)

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
