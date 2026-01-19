from collections import defaultdict

def cluster_errors(errors):
    clusters = defaultdict(list)
    for e in errors:
        key = e.split(" ")[-1][:30]
        clusters[key].append(e)
    print(f"🧠 Clustered into {len(clusters)} groups")
    return dict(clusters)
