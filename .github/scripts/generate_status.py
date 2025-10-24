import os
import json
import requests
from datetime import datetime

# Directory to store JSON badges
os.makedirs(".github/data", exist_ok=True)

# ------------------------------
# Example “live system” metrics
# ------------------------------
# Uptime (simulate since repo creation)
repo_creation = datetime(2025, 1, 1)
now = datetime.now()
uptime_days = (now - repo_creation).days
uptime_percent = min(100, 90 + uptime_days % 10)

# Ping (simulate a server ping)
ping_ms = 15 + uptime_days % 10

# Memory usage (simulate)
memory_mb = 512 + uptime_days % 256

# Visitors (use GitHub Page views if desired)
# For now, simple simulation
visitors = 1000 + uptime_days * 3

# Function to save shields JSON
def save_shield(filename, label, message, color):
    data = {
        "schemaVersion": 1,
        "label": label,
        "message": message,
        "color": color
    }
    with open(f".github/data/{filename}", "w") as f:
        json.dump(data, f)

# Create badges
save_shield("status.json", "SYSTEM STATUS", "Online ✅", "d79921")
save_shield("uptime.json", "UPTIME", f"{uptime_percent}%", "98971A")
save_shield("ping.json", "PING", f"{ping_ms}ms", "458588")
save_shield("memory.json", "MEMORY", f"{memory_mb}MB cache", "B16286")
save_shield("visitors.json", "VISITORS", f"{visitors}", "FABD2F")
