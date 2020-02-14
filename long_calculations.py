from time import time


def add(a, b):
    a, b = a[::-1], b[::-1]
    res = ''

    max_len = max(len(a), len(b))
    a, b = a.ljust(max_len, '0'), b.ljust(max_len, '0')

    shift = 0
    for i in range(max_len):
        da, db = int(a[i]), int(b[i])
        temp = da + db + shift

        shift = temp // 10
        res += str(temp % 10)

    if shift:
        res += '1'

    return res[::-1].lstrip('0')


def subtract(a, b):  # a - b = res; a > b
    a, b = sorted([a, b], key=lambda x: (len(x), x), reverse=True)
    max_len = len(a)
    a, b = a.rjust(max_len, '0'), b.rjust(max_len, '0')

    a, b = list(map(int, list(a[::-1]))), list(map(int, list(b[::-1])))

    for i in range(max_len):
        da, db = a[i], b[i]
        a[i] = da - db

    return ''.join(map(str, normalize(a)))[::-1].lstrip('0')


def normalize(a):
    for i in range(len(a)):
        if a[i] < 0:
            a[i + 1] -= 1
            a[i] += 10
        elif a[i] >= 10:
            a[i + 1] += a[i] // 10
            a[i] %= 10

    return a


def multiply(a, b):
    a, b = a[::-1], b[::-1]
    res = [0] * (len(a) + len(b))
    for i in range(len(a)):
        for j in range(len(b)):
            da, db = int(a[i]), int(b[j])
            res[i + j] += da * db

    ans = ''.join(map(str, normalize(res)))[::-1].lstrip('0')
    return ans if ans else '0'


def karatsuba_multiply(a, b):
    if len(a) < 5 and len(b) < 5:
        return multiply(a, b)
    else:
        max_len = max(len(a), len(b))
        n = max_len // 2
        if max_len % 2 != 0:
            n += 1
        a0, b0 = a[-n:].lstrip('0'), b[-n:].lstrip('0')
        a1, b1 = a[:-n], b[:-n]

        sa = 1 if max(a0, a1, key=lambda x: (len(x), x)) == a0 else -1
        sb = 1 if max(b0, b1, key=lambda x: (len(x), x)) == b0 else -1

        c0 = karatsuba_multiply(a0, b0)
        c1 = karatsuba_multiply(a1, b1)
        c2 = karatsuba_multiply(subtract(a0, a1), subtract(b0, b1))

        if sa == sb:
            return add(add(c0, c1 + ('0' * (2 * n))), subtract(add(c0, c1), c2) + ('0' * n))
        else:
            return add(add(c0, c1 + ('0' * (2 * n))), add(add(c0, c1), c2) + ('0' * n))


f = open('input_lc.txt', 'r')
nums = f.readlines()
f.close()

n1, n2 = map(str.strip, nums)
print("addition")
print(add(n1, n2))
print(sum(map(int, [n1, n2])))
print(sum(map(int, [n1, n2])) == int(add(n1, n2)))

print()

print("subtraction")
print(subtract(n1, n2))
print(max(map(int, [n1, n2])) - min(map(int, [n1, n2])))
print(str(max(map(int, [n1, n2])) - min(map(int, [n1, n2]))) == subtract(n1, n2))

print()

print("multiplication")
t = time()
print(multiply(n1, n2))
print("time is:", time() - t)
print(int(n1) * int(n2))
print(str(int(n1) * int(n2)) == multiply(n1, n2))

print()

print("karatsuba multiplication")
t = time()
print(karatsuba_multiply(n1, n2))
print("time is:", time() - t)
print(int(n1) * int(n2))
print(str(int(n1) * int(n2)) == karatsuba_multiply(n1, n2))
