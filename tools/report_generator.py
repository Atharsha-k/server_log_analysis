import os
from datetime import datetime

def generate_report(state):
    os.makedirs("outputs/reports", exist_ok=True)

    path = f"outputs/reports/report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"

    with open(path, "w") as f:
        f.write("EXECUTIVE SUMMARY\n")
        f.write(state["summary"])
        f.write("\n\nIMPACT\n")
        f.write(state["impact"])

    print(f"📄 Report generated: {path}")
    return path
