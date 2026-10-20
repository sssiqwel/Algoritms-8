capacity = 8
items = [
    (3, 4),
    (5, 7),
    (2, 2),
]

best = [None] * (capacity + 1)
best[0] = (0, 0)
for current in range(1, capacity + 1):
    chosen = None
    for weight, profit in items:
        previous = current - weight
        if previous < 0 or best[previous] is None:
            continue
        candidate_profit = best[previous][0] + profit
        candidate_count = best[previous][1] + 1
        if (
            chosen is None
            or candidate_profit > chosen[0]
            or (candidate_profit == chosen[0] and candidate_count < chosen[1])
        ):
            chosen = (candidate_profit, candidate_count)
    best[current] = chosen

if best[capacity] is None:
    print(-1)
else:
    print(best[capacity][0], best[capacity][1])
