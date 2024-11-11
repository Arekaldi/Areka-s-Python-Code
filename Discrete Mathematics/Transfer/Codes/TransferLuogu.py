NumberInput = input()
n = int(NumberInput)

Map = []

for i in range(1, n + 1):
    NumberInput = input()
    row = list(map(int, NumberInput.split()))
    Map.append(row)
for k in range(n):
    for i in range(n):
        for j in range(n):
                Map[i][j] |= Map[i][k] & Map[k][j]

for i in range(n):
    for j in range(n):
        print(Map[i][j], end=" ")
    print()
