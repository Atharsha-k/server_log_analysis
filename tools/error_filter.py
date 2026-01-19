def filter_errors(logs):
    errors = [l for l in logs if "error" in l.lower() or "500" in l]
    print(f"❌ Found {len(errors)} error logs")
    return errors
