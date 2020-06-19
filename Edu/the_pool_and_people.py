f = open("input_the_pool_and_people.txt", 'r')
data = f.readlines()
f.close()

xs, ys = 0, 0
dist = 0
x, y = map(int, data.pop(0).split())
n = int(data.pop(0))
people = [0] * n

for i in range(n):
    people[i] = list(map(int, data.pop(0).split()))

while people:
    xc, yc = people[0]
    index = 0
    min_dist = 10 ** 9
    for i in range(len(people)):
        if min_dist > ((xs - people[i][0]) ** 2 + (ys - people[i][1]) ** 2) ** 0.5:
            xc, yc = people[i]
            min_dist = ((xs - xc) ** 2 + (ys - yc) ** 2) ** 0.5
            index = i

    dist += min_dist
    edge = [y - yc, yc, x - xc, xc]
    min_edge = min(edge)
    if edge.index(min_edge) == 0:
        xs = xc
        ys = y
    elif edge.index(min_edge) == 1:
        xs = xc
        ys = 0
    elif edge.index(min_edge) == 2:
        xs = x
        ys = yc
    elif edge.index(min_edge) == 3:
        xs = 0
        ys = yc

    people.pop(index)
    dist += min_edge

print(dist)
