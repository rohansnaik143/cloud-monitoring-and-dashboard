# memory_stress.py
a = []
while True:
    a.append(' ' * 10**6)  # allocate ~1MB repeatedly
