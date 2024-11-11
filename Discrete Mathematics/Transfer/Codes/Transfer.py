NumberInput = input()

n, m = map(int, NumberInput.split())

Map = []

for i in range(1, n + 1):
    row = list([0] * (n + 1))
    Map.append(row)

for i in range(m):
    NumberInput = input()
    u, v = map(int, NumberInput.split())
    Map[u - 1][v - 1] = 1
for k in range(n):
    for i in range(n):
        for j in range(n):
                Map[i][j] |= Map[i][k] & Map[k][j]

for i in range(n):
    for j in range(n):
        if(Map[i][j]):
            print(i + 1, j + 1)
