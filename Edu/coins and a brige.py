f = open("input1.txt", mode="r")
f = f.readlines()
x, y = map(int, f.pop(0).split())
z = int(f.pop(0))
max_sum = x * 100 + y
max_i = 0

for i in range(1, 10001):
    c = x * 100 + y - z
    if c < 0:
        break
    x, y = c % 100, c // 100
    if c > max_sum:
        max_sum = c
        max_i = i

print(max_sum // 100, max_sum % 100)
print(max_i)
