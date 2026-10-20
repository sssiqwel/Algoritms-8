heights = [10, 30, 40, 20]
n = len(heights)

cost = [0] * n
cost[1] = abs(heights[1] - heights[0])
for i in range(2, n):
    one_step = cost[i - 1] + abs(heights[i] - heights[i - 1])
    two_step = cost[i - 2] + abs(heights[i] - heights[i - 2])
    cost[i] = min(one_step, two_step)

print(cost[-1])
