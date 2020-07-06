def bfs(v):
    if v in visited:
        return
    visited.add(v)
    bfs_list.append(v)
    for i in adj[v]:
        if i not in visited:
            queue.append(i)
    while queue:
        bfs(queue.pop(0))


f = open("input_dfs.txt", 'r')
data = f.readlines()
f.close()

adj = dict()
visited = set()
queue = list()
bfs_list = list()

n_vert, n_edges = map(int, data.pop(0).split())
for i in range(n_vert):
    adj[i + 1] = []
for _ in range(n_edges):
    a, b = map(int, data.pop(0).split())
    adj[a].append(b)
    adj[b].append(a)

start = 1
bfs(start)
print(bfs_list)
