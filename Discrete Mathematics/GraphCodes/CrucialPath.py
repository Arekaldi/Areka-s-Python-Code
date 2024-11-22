import copy
import functools

inputNumber = input().split()
n = int(inputNumber[0])
m = int(inputNumber[1])
s = int(inputNumber[2])
t = int(inputNumber[3])

map = [[-1 for j in range(0, n + 1)] for i in range(0, n + 1)]
inDegree = [0 for i in range(0, n + 1)]
for i in range(0, m):
    inputLine = input().split()
    u = int(inputLine[0])
    v = int(inputLine[1])
    w = int(inputLine[2])
    map[u][v] = w
    inDegree[v] += 1

def topologicalSort():
    result = []
    queue = []
    for i in range(1, n + 1):
        if inDegree[i] == 0:
            result.append(i)
            queue.append(i)
    while len(queue) > 0:
        u = queue.pop(0)
        for v in range(1, n + 1):
            if map[u][v] != -1:
                inDegree[v] -= 1
                if inDegree[v] == 0:
                    result.append(v)
                    queue.append(v)
                if etv[v] < etv[u] + map[u][v]:
                    etv[v] = etv[u] + map[u][v]
    endPoint = result.pop(n - 1)
    for i in range(1, n + 1):
        ltv[i] = etv[endPoint]
    while len(result) > 0:
        u = result.pop(len(result) - 1)
        for v in range(1, n + 1):
            if map[u][v] != -1:
                if ltv[u] > ltv[v] - map[u][v]:
                    ltv[u] = ltv[v] - map[u][v]

etv = [0 for i in range(0, n + 1)]
ltv = [0 for i in range(0, n + 1)]

topologicalSort()

vis = [0 for i in range(0, n + 1)]
outputArray = [s]
Arraylist = []

def findCriticalPath(now):
    if now == t:
        Arraylist.append(copy.deepcopy(outputArray))
        return
    for v in range(1, n + 1):
        if map[now][v] == -1:
            continue
        if vis[v] == 1:
            continue
        ete = etv[now]
        lte = ltv[v] - map[now][v]
        if ete == lte:
            outputArray.append(v)
            vis[v] = 1
            findCriticalPath(v)
            vis[v] = 0
            outputArray.pop(len(outputArray) - 1)

print(ltv[t] - ltv[s])
for i in range(1, n + 1):
    print(etv[i], ltv[i], ltv[i] - etv[i])

findCriticalPath(s)

def compareTo(x, y):
    for i in range(1, len(x)):
        if x[i] < y[i]:
            return 1
        elif x[i] > y[i]:
            return -1
    return 0

def cmp(x, y):
    if len(x) < len(y):
        return 1
    elif len(x) > len(y):
        return -1
    else:
        return compareTo(x, y)

Arraylist.sort(key=functools.cmp_to_key(cmp), reverse=True)

for i in range(len(Arraylist)):
    for j in range(len(Arraylist[i])):
        print(Arraylist[i][j], end=' ')
    print()