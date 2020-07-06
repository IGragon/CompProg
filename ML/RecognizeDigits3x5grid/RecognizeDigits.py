from random import randint

n, m = 3, 5
outputs = 10
weights = [[] for _ in range(outputs)]
weights_are_loaded = False
learning_data = []


def init():
    global weights_are_loaded
    try:
        f = open("weights.txt", 'r')
        data = f.readlines()
        f.close()
        for i in range(outputs):
            for _ in range(m):
                row = data.pop(0)
                row = list(map(int, row.split()))
                weights[i] += row
            data.pop(0)
        weights_are_loaded = True
    except Exception:
        for i in range(outputs):
            for _ in range(m):
                row = [randint(6, 14) for _ in range(n)]
                weights[i] += row


def get_result(i, input_data):
    ans = 0
    for j in range(n * m):
        ans += input_data[j] * weights[i][j]
    return ans


def correct_weights(mode, i, input_data):  # mode == True - не узнал своего, mode == False - узнал не своего
    if mode:
        for j in range(n * m):
            weights[i][j] += input_data[j]
    else:
        for j in range(n * m):
            weights[i][j] -= input_data[j]


def save_weights():
    f = open("weights.txt", 'w')
    for i in range(outputs):
        for j in range(0, n * m, 3):
            f.write('\t'.join(map(str, weights[i][j:j + 3])) + '\n')
        f.write('\n')


def start_learning():
    f = open("learning_dataset.txt", 'r')
    data = f.readlines()
    f.close()
    t = int(data.pop(0))
    for _ in range(t):
        right_ans = int(data.pop(0))
        results = [0] * outputs
        input_data = []
        for _ in range(m):
            row = list(map(int, list(data.pop(0).strip())))
            input_data += row
        for i in range(outputs):
            results[i] = get_result(i, input_data)
        ans = results.index(max(results))
        if ans != right_ans:
            correct_weights(True, right_ans, input_data)
            correct_weights(False, ans, input_data)
    save_weights()


def get_answer(data):
    input_data = []
    results = [0] * outputs
    for row in data:
        input_data += list(map(int, list(row)))
    for i in range(outputs):
        results[i] = get_result(i, input_data)
    return results.index(max(results))


def test():
    input_data = []
    while len(input_data) != m:
        input_data.append(list(input()))
    print("Res:", get_answer(input_data))



init()
if not weights_are_loaded:
    start_learning()
else:
    print("Weights are loaded")

f = open("validation_dataset.txt", 'r')
validation_data = list(map(str.strip, f.readlines()))
f.close()
t = int(validation_data.pop(0))
for _ in range(t):
    print("Exp:", validation_data.pop(0), end=" ")
    data = [validation_data.pop(0) for _ in range(m)]
    print("Got:", get_answer(data))

while True:
    test()
