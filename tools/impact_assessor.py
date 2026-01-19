def assess_impact(state):
    error_count = len(state["errors"])
    if error_count > 1000:
        return "HIGH impact – possible outage"
    elif error_count > 100:
        return "MEDIUM impact – degraded performance"
    else:
        return "LOW impact"
