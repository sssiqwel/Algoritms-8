s = "abc"
t = "acb"

n = len(s)
m = len(t)
need = [[0] * (m + 1) for _ in range(n + 1)]
for i in range(n, -1, -1):
    for j in range(m, -1, -1):
        if i == n and j == m:
            need[i][j] = 0
        elif i == n:
            need[i][j] = m - j
        elif j == m:
            need[i][j] = n - i
        elif s[i] == t[j]:
            need[i][j] = 1 + need[i + 1][j + 1]
        else:
            need[i][j] = 1 + min(need[i + 1][j], need[i][j + 1])

i = 0
j = 0
result = []
while i < n or j < m:
    if i == n:
        result.append(t[j])
        j += 1
    elif j == m:
        result.append(s[i])
        i += 1
    elif s[i] == t[j]:
        result.append(s[i])
        i += 1
        j += 1
    else:
        can_take_s = need[i][j] == 1 + need[i + 1][j]
        can_take_t = need[i][j] == 1 + need[i][j + 1]
        if can_take_s and (not can_take_t or s[i] <= t[j]):
            result.append(s[i])
            i += 1
        else:
            result.append(t[j])
            j += 1

print("".join(result))
