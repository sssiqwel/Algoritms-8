s = "abcde"
t = "ace"

n = len(s)
m = len(t)
length = [[0] * (m + 1) for _ in range(n + 1)]
for i in range(1, n + 1):
    for j in range(1, m + 1):
        if s[i - 1] == t[j - 1]:
            length[i][j] = length[i - 1][j - 1] + 1
        else:
            length[i][j] = max(length[i - 1][j], length[i][j - 1])

print(length[n][m])
