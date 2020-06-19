f = open("input_owYes.txt", 'r')
data = f.readlines()
f.close()

k = int(data.pop(0))
n = int(data.pop(0))
vert = dict()

for i in range(k):
    vert[i + 1] = []

for _ in range(n):
    a, b = map(int, data.pop(0).split())
    vert[a].append(b)
    vert[b].append(a)

isEulerianPath = True
odd_vert = -1
count_odd_vert = 0
for v in vert:
    if len(vert[v]) % 2 == 1:
        count_odd_vert += 1
        odd_vert = v
    if count_odd_vert > 2:
        isEulerianPath = False
        break

if isEulerianPath:
    print("YES")
    path = []
    if odd_vert >= 0:
        current_pos = odd_vert
    else:
        current_pos = list(vert.keys())[0]
    path.append(current_pos)

    while any(map(lambda x: len(x) > 0, vert.values())):
        if len(vert[current_pos]) > 1 and len(vert[vert[current_pos][-1]]) % 2 == 1:
            next_pos = vert[current_pos].pop(-2)
        else:
            next_pos = vert[current_pos].pop()
        del vert[next_pos][vert[next_pos].index(current_pos)]
        path.append(next_pos)
        current_pos = next_pos
    print('-'.join(map(str, path)))
else:
    print("NO")
