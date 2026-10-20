capacity = 10
items = [
    (6, 5),
    (5, 4),
    (5, 6),
    (4, 3),
]

best = [0] * (capacity + 1)
for weight, value in items:
    for current in range(capacity, weight - 1, -1):
        candidate = best[current - weight] + value
        if candidate > best[current]:
            best[current] = candidate

print(best[capacity])
