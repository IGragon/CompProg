from random import randint as rint

a = ''
b = ''
for i in range(1000):
    a += str(rint(0, 10))
    b += str(rint(0, 10))
print(a)
print(b)