import socket
import time
import random
from datetime import datetime, timezone

WAZUH_HOST = "wazuh.manager"
PORT = 514  # syslog UDP

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

def ts():
    return datetime.now(timezone.utc).strftime("%b %d %H:%M:%S")

HOST = "ubuntu-server"

ATTACKS = [
    # SSH Brute Force
    lambda: f"{ts()} {HOST} sshd[2221]: Failed password for invalid user admin from 203.0.113.{random.randint(10,99)} port {random.randint(30000,60000)} ssh2",

    # Successful login after brute force
    lambda: f"{ts()} {HOST} sshd[2221]: Accepted password for root from 203.0.113.{random.randint(10,99)} port {random.randint(30000,60000)} ssh2",

    # Port scan detected
    lambda: f"{ts()} {HOST} kernel: [UFW BLOCK] IN=eth0 SRC=198.51.100.{random.randint(10,99)} DST=192.168.1.10 PROTO=TCP DPT={random.choice([22,80,443,3306])}",

    # Suspicious sudo privilege escalation
    lambda: f"{ts()} {HOST} sudo: student : TTY=pts/0 ; PWD=/home/student ; USER=root ; COMMAND=/bin/bash",

    # PowerShell execution (Windows-style, Wazuh still flags)
    lambda: f"{ts()} {HOST} powershell[4432]: powershell.exe -enc SQBtAG8AdgBlAC0AVwBlAGIAUgBlAHEAdQBlAHMAdA==",

    # Data exfiltration
    lambda: f"{ts()} {HOST} kernel: Outbound connection to suspicious IP 45.67.89.{random.randint(10,99)} over port 4444"
]

print("🚨 SOC Telemetry Generator Started", flush=True)

while True:
    msg = random.choice(ATTACKS)()
    syslog = f"<134>{msg}"
    sock.sendto(syslog.encode(), (WAZUH_HOST, PORT))
    print("SENT:", syslog, flush=True)
    time.sleep(random.randint(1,3))
