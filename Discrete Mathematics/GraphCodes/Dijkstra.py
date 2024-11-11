inputString = input()
n = int(inputString.split()[0])
m = int(inputString.split()[1])
s = int(inputString.split()[2])
t = int(inputString.split()[3])

graph = [[0 for i in range(n+1)] for j in range(n+1)]
def addEdge(u, v, w):
    graph[u][v] = w
    graph[v][u] = w

for i in range(m):
    addEdge(*map(int, input().split()))
    # add edge u -> v with weight w

# Dijkstra's algorithm
dist = [float('inf')] * (n+1)
dist[s] = 0
visited = [False] * (n+1)

for i in range(n):
    u = -1
    for j in range(1, n+1):
        if not visited[j] and (u == -1 or dist[j] < dist[u]):
            u = j
    if u == -1:
        break
    visited[u] = True
    for v in range(1, n+1):
        if not visited[v] and graph[u][v] != 0 and dist[u] + graph[u][v] < dist[v]:
            dist[v] = dist[u] + graph[u][v]
road = [0 for i in range(n+1)]
last = t
tot = 1
while last != s:
    for i in range(1, n + 1):
        if graph[last][i] != 0 and dist[last] - graph[last][i] == dist[i]:
            road[last] = i
            last = i
            tot += 1
            break
last = t
ans = []
while last != s:
    ans.append(last)
    last = road[last]
ans.append(s)
ans.reverse()
print(dist[t])
for i in ans:
    print(i, end=' ')