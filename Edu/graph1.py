f = open("input.txt")

f = f.readlines()

k = int(f[0])

start_point, end_point = map(int, f[1].split())
start_point -= 1
end_point -= 1
edges = [[0 for _ in range(k)] for _ in range(k)]
points = [0 for _ in range(k)]

points[start_point] = 1

for i in range(int(f[2])):
    m, n = list(map(int, f[3 + i].split()))
    m -= 1
    n -= 1
    edges[m][n] = 1
    edges[n][m] = 1

#print(points)
#for line in edges:
 #   print(line)

somethingChanged = True

while points[end_point] != 1 and somethingChanged:
    somethingChanged = False

    for i in range(k):
        for j in range(k):
            if points[i] == 1 and edges[i][j] == 1 and points[j] == 0:
                points[j] = 1
                somethingChanged = True
    print(points)

print("YES" if points[end_point] == 1 else "NO")
