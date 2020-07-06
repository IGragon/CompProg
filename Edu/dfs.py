def dfs(v):
    if v in visited:
        return
    visited.append(v)
    for i in adj[v]:
        if i not in visited:
            dfs(i)


f = open("input_dfs.txt", 'r')
data = f.readlines()
f.close()

adj = dict()
visited = list()

n_vert, n_edges = map(int, data.pop(0).split())
for i in range(n_vert):
    adj[i + 1] = []
for _ in range(n_edges):
    a, b = map(int, data.pop(0).split())
    adj[a].append(b)
    adj[b].append(a)

start = 1
dfs(start)
print(visited)
