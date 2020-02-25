f = open("input.txt")

f = f.readlines()

n, m = map(int, f.pop(0).split())

field = [[-3 for _ in range(n + 2)] for _ in range(m + 2)]

field[0] = [-1 for _ in range(n + 2)]
field[-1] = [-1 for _ in range(n + 2)]

for i in range(m + 2):
    field[i][0] = -1
    field[i][-1] = -1

for k in range(int(f.pop(0))):
    x, y = map(int, f.pop(0).split())
    field[y + 1][x + 1] = -1

xs, ys = map(int, f.pop(0).split())
field[ys + 1][xs + 1] = -2


xf, yf = map(int, f.pop(0).split())
field[yf + 1][xf + 1] = 0

for s in field:
    print(s)

step = 1
flag = True
while field[ys + 1][xs + 1] < 0 and flag:
    flag = False
    for j in range(n):
        for i in range(m):
            if field[i + 1][j + 1] < -1:
                if field[i][j + 1] == step - 1:
                    field[i + 1][j + 1] = step
                    flag = True
                elif field[i + 2][j + 1] == step - 1:
                    field[i + 1][j + 1] = step
                    flag = True
                elif field[i + 1][j] == step - 1:
                    field[i + 1][j + 1] = step
                    flag = True
                elif field[i + 1][j + 2] == step - 1:
                    field[i + 1][j + 1] = step
                    flag = True
    step += 1

    print()
    for s in field:
        print(s)

if field[ys + 1][xs + 1] == - 2:
    print("NO")
else:
    print(step - 1)
