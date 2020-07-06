INF = 10 ** 10

f = open("dijkstra.in", 'r')
data = f.readlines()
f.close()

n, s, f = map(int, data.pop(0).split())
s -= 1
f -= 1

visited = set()
adj_matrix = []
edges = [INF for _ in range(n)]
used = [False for _ in range(n)]
for _ in range(n):
    adj_matrix.append(list(map(int, data.pop(0).split())))

edges[s] = 0
min_dist = 0
min_vertex = s
while min_dist < INF:
    i = min_vertex
    used[i] = True
    for j in range(n):
        if adj_matrix[i][j] > 0:
            if edges[i] + adj_matrix[i][j] < edges[j]:
                edges[j] = edges[i] + adj_matrix[i][j]
    min_dist = INF
    for j in range(n):
        if not used[j] and edges[j] < min_dist:
            min_dist = edges[j]
            min_vertex = j
print(edges[f] if edges[f] < INF else -1)
