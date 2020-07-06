f = open("input_ta.txt", 'r')
data = f.readlines()
f.close()

r, n = map(int, data.pop(0).split())
interchanges = []
for _ in range(r):
    order = data.pop(0).strip()
    value = data.pop(0).strip()
    interchanges.append((order, value))

text = []
for _ in range(n):
    text.append(data.pop(0))

interchanges = sorted(interchanges, key=lambda x: len(x[0]))
for i in range(n):
    for j in range(r):
        text[i] = text[i].replace(interchanges[j][0], interchanges[j][1])
    print(text[i], end='')
