# case_memory/log_memory.py

import os
import json
from datetime import datetime

LOG_DIR = "./case_memory/memory_logs"
os.makedirs(LOG_DIR, exist_ok=True)

def log_memory(content, category="note", source="operator"):
    today = datetime.now().strftime("%Y-%m-%d")
    log_path = os.path.join(LOG_DIR, f"log_{today}.json")

    entry = {
        "timestamp": datetime.now().isoformat(),
        "category": category,
        "source": source,
        "content": content
    }

    data = []
    if os.path.exists(log_path):
        with open(log_path, "r") as f:
            data = json.load(f)

    data.append(entry)

    with open(log_path, "w") as f:
        json.dump(data, f, indent=2)

    print(f"Logged memory: {content[:60]}...")
    return entry
