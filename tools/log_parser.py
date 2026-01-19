def parse_logs(path: str):
    logs = []
    with open(path, "r", errors="ignore") as f:
        for line in f:
            logs.append(line.strip())
    print(f"📄 Parsed {len(logs)} lines")
    return logs
