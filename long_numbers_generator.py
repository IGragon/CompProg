from random import randint as rint
for i in range(2):
    n = str(rint(1, 9))
    for _ in range(999):
        n += str(rint(0, 9))
    print(int(n))
