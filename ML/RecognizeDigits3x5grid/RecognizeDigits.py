from random import randint


class Model:

    def __init__(self):
        self.n, self.m = 3, 5
        self.outputs = 10
        self.weights = [[] for _ in range(self.outputs)]
        self.weights_are_loaded = False
        self.learning_data = []

        global weights_are_loaded
        try:
            f = open("weights.txt", 'r')
            data = f.readlines()
            f.close()
            for i in range(self.outputs):
                for _ in range(self.m):
                    row = data.pop(0)
                    row = list(map(int, row.split()))
                    self.weights[i] += row
                data.pop(0)
            weights_are_loaded = True
        except Exception:
            for i in range(self.outputs):
                for _ in range(self.m):
                    row = [randint(6, 14) for _ in range(self.n)]
                    self.weights[i] += row

    def get_result(self, i, input_data):
        ans = 0
        for j in range(self.n * self.m):
            ans += input_data[j] * self.weights[i][j]
        return ans

    def correct_weights(self, mode, i, input_data):  # mode == True - не узнал своего, mode == False - узнал не своего
        if mode:
            for j in range(self.n * self.m):
                self.weights[i][j] += input_data[j]
        else:
            for j in range(self.n * self.m):
                self.weights[i][j] -= input_data[j]

    def save_weights(self):
        f = open("weights.txt", 'w')
        for i in range(self.outputs):
            for j in range(0, self.n * self.m, 3):
                f.write('\t'.join(map(str, self.weights[i][j:j + 3])) + '\n')
            f.write('\n')

    def start_learning(self):
        f = open("learning_dataset.txt", 'r')
        data = f.readlines()
        f.close()
        t = int(data.pop(0))
        for _ in range(t):
            right_ans = int(data.pop(0))
            results = [0] * self.outputs
            input_data = []
            for _ in range(self.m):
                row = list(map(int, list(data.pop(0).strip())))
                input_data += row
            for i in range(self.outputs):
                results[i] = self.get_result(i, input_data)
            ans = results.index(max(results))
            if ans != right_ans:
                self.correct_weights(True, right_ans, input_data)
                self.correct_weights(False, ans, input_data)
        self.save_weights()

    def make_prediction(self, data):
        results = [0] * self.outputs
        for i in range(self.outputs):
            results[i] = self.get_result(i, data)
        return results.index(max(results))

    def test(self):
        data = []
        while len(data) != self.m:
            data.append(list(input()))

        input_data = []
        for row in data:
            input_data += list(map(int, list(row)))
        print("Res:", self.make_prediction(input_data))
#
#
# model = Model()
#
# if not weights_are_loaded:
#     model.start_learning()
# else:
#     print("Weights are loaded")
#
# f = open("validation_dataset.txt", 'r')
# validation_data = list(map(str.strip, f.readlines()))
# f.close()
# t = int(validation_data.pop(0))
# for _ in range(t):
#     print("Exp:", validation_data.pop(0), end=" ")
#     data = [validation_data.pop(0) for _ in range(model.m)]
#     input_data = []
#     for row in data:
#         input_data += list(map(int, list(row)))
#     print("Got:", model.make_prediction(input_data))
#
# while True:
#     model.test()
