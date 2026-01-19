import os

def find_log_file(path: str):
    if not os.path.exists(path):
        raise FileNotFoundError("Log file not found")
    print(f"✅ Log file found: {path}")
    return path
