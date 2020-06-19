# погуглить длинную арифметику в питоне
# а лучше поделать самому


def add(a, b):
    a, b = str(a)[::-1], str(b)[::-1]

    max_len = max(len(a), len(b))
    a, b = a.ljust(max_len, '0'), b.ljust(max_len, '0')

    shift = 0
    res = ''
    for i in range(max_len):
        da, db = int(a[i]), int(b[i])

        temp = da + db + shift
        res += str(temp % 10)
        shift = temp // 10

    if shift:
        res += '1'

    return res[::-1]


def karatsuba_multiply(a, b):
    a, b = str(a), str(b)
    max_len = max(len(a), len(b))
    x = 10 ** (max_len // 2)

    a, b = int(a), int(b)

    if max_len < 5:
        return a * b
    else:
        a0, b0 = a % x, b % x
        a1, b1 = a // x, b // x

        c0 = karatsuba_multiply(a0, b0)
        c1 = karatsuba_multiply(a1, b1)
        c2 = karatsuba_multiply(abs(a0 - a1), abs(b0 - b1))
        return c0 + (c0 + c1 - c2) * x + c1 * x ** 2


def multiply(a, b):
    a, b = str(a)[::-1], str(b)[::-1]
    res = [0] * (len(a) + len(b))
    for i in range(len(a)):
        for j in range(len(b)):
            res[i + j] += int(a[i]) * int(b[j])
    return ''.join(map(str, normalize(res)[::-1]))


def normalize(a):
    for i in range(len(a)):
        if a[i] > 10:
            a[i + 1] += a[i] // 10
            a[i] = a[i] % 10
    return a



f = open("input_nums.txt", 'r')
nums = f.readlines()
f.close()

num1 = int(nums.pop(0).strip())
num2 = int(nums.pop(0).strip())

print(add(karatsuba_multiply(num1, num1), karatsuba_multiply(num2, num2)))
print(add(multiply(num1, num1), multiply(num2, num2)))
print(num1 ** 2 + num2 ** 2)
