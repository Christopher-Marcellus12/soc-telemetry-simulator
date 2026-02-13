# 🛡️ Wazuh SOC Telemetry Simulator

![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)
![Python](https://img.shields.io/badge/Python-3.x-blue)
![Docker](https://img.shields.io/badge/Docker-Containerized-2496ED?logo=docker&logoColor=white)
![Wazuh](https://img.shields.io/badge/SIEM-Wazuh-green)
![Cybersecurity](https://img.shields.io/badge/BlueTeam-SOC%20Lab-red)
![Status](https://img.shields.io/badge/Project-Active-success)

A Dockerized **Security Operations Center (SOC)** lab built using **Wazuh SIEM** and a custom Python telemetry generator that emits realistic security events.

This project simulates real-world attack activity for **threat hunting**, **incident detection**, and **blue-team training**.

---

## 🚀 Overview

The SOC Telemetry Simulator generates realistic logs such as:

- SSH brute-force attempts
- Network scanning activity
- Privilege escalation behavior
- Suspicious command execution

These events are ingested into Wazuh to simulate a live security monitoring environment.

---

## 🧠 Skills Demonstrated

- SIEM Monitoring (Wazuh)
- SOC Workflow Simulation
- Threat Detection & Analysis
- Docker Infrastructure
- Python Automation
- Log Telemetry Engineering
- Security Event Simulation
- Blue-Team Operations

---

## 🏗️ Architecture
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

<img width="1512" height="949" alt="Screenshot 2026-02-12 at 9 05 35 PM" src="https://github.com/user-attachments/assets/0557b0f3-46cd-4bd0-9973-b87dca17cf19" />

<img width="842" height="396" alt="Screenshot 2026-02-12 at 9 04 35 PM" src="https://github.com/user-attachments/assets/29163ea4-27d9-416d-a1e8-8e9885a4e2ec" />
