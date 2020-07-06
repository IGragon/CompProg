from random import randint

n, m = 3, 5
weights = [0] * (n * m)


def init():
    for i in range(n * m):
        weights[i] = randint(6, 14)


def start_learning():
    f = open("dataset_r5.txt")
    data = list(map(str.strip, f.readlines()))
    f.close()
    t = int(data.pop(0))
    for _ in range(t):
        ans = int(data.pop(0))
        result_exp = int(ans == 5)
        input_data = []
        for i in range(m):
            row = data.pop(0)
            for val in row:
                input_data.append(int(val))
        result = get_result(input_data)
        k = result_exp - result
        if k > 0:
            for i in range(n * m):
                if input_data[i] == 1:
                    weights[i] += 1
        elif k < 0:
            for i in range(n * m):
                if input_data[i] == 1:
                    weights[i] -= 1


def get_result(input_data):
    ans = 0
    for i in range(n * m):
        ans += input_data[i] * weights[i]
    return 1 if ans > 100 else 0


def is_it_five(data):
    input_data = []
    for i in range(m):
        row = data.pop(0)
        for val in row:
            input_data.append(int(val))
    return get_result(input_data)


init()
start_learning()
f = open("validation_data_r5.txt", 'r')
validation_data = list(map(str.strip, f.readlines()))
f.close()
t = int(validation_data.pop(0))
for _ in range(t):
    print(validation_data.pop(0), end=" ")
    data = [validation_data.pop(0) for _ in range(m)]
    print(is_it_five(data))

for i in range(0, n * m, n):
    print(weights[i:i + n])
