f = open("input_owNo.txt", 'r')
data = f.readlines()
f.close()

k = int(data.pop(0))
n = int(data.pop(0))
edges = [[0 for _ in range(k)] for _ in range(k)]
nodes = [0 for i in range(k)]
for _ in range(n):
    a, b = map(int, data.pop(0).split())
    edges[a - 1][b - 1] = 1
    edges[b - 1][a - 1] = 1

num_of_edges = list(map(lambda x: x.count(1), edges))
count = 0
eulerianPath = True
for i in num_of_edges:
    if i % 2:
        count += 1
    if count > 2:
        eulerianPath = False
        break

print("YES" if eulerianPath else "NO")
