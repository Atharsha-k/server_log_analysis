from collections import Counter

def analyze_frequency(errors):
    counter = Counter(errors)
    return counter.most_common(10)
