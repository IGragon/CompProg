f = open("input.txt", mode="r")
f = f.readlines()

m, n = map(int, f.pop(0).split())
a, b = 1, 1
nums = set()
nums.add(a)
d = 0
while a < m:
    d += 1
    a += 1
    while a in nums:
        a += 1
    b = a + d
    nums.add(a)
    nums.add(b)
    print(a, b)

if a == m and b == n:
    print(2)
else:
    print(1)
