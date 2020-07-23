from random import randint
from time import time


class Model:
    def __init__(self, file_weights="weights.txt", file_save="weights.txt", input_neurons=28 * 28, hidden_neurons=50,
                 output_neurons=4):
        self.file_weights = file_weights
        self.file_save = file_save
        self.layers = [input_neurons, hidden_neurons, output_neurons]
        self.weights = [[[0 for _ in range(input_neurons)] for _ in range(hidden_neurons)],
                        [[0 for _ in range(hidden_neurons)] for _ in range(output_neurons)]]
        self.load_weights()

    def load_weights(self):
        try:
            f_weights = open(self.file_weights, 'r')
            data = f_weights.readlines()
            f_weights.close()

            for i in range(len(self.layers) - 1):
                for j in range(self.layers[i + 1]):
                    row = data.pop(0)
                    row = list(map(float, row.split()))
                    self.weights[i][j] = row
            print("Weights are loaded")
        except Exception:
            self.generate_weights()

    def save_weights(self):
        f_save = open(self.file_save, 'w')
        for group in self.weights:
            for neuron in group:
                f_save.write(' '.join(map(str, neuron)) + '\n')
        f_save.close()

    def generate_weights(self):
        for i in range(len(self.layers) - 1):
            for j in range(self.layers[i + 1]):
                for k in range(self.layers[i]):
                    self.weights[i][j][k] = randint(6, 14)

    def weight_function(self, input_data, group, neuron, r=1):
        s = 0
        for i in range(len(input_data)):
            s += input_data[i] * self.weights[group][neuron][i] * r
        return int(s > 5200)

    def correct_weights(self, group, neuron, data, val, r=1):
        for i in range(len(self.weights[group][neuron])):
            self.weights[group][neuron][i] += data[i] * val * r

    def normalize(self, data):
        abs_sum = sum(map(float.__abs__, data))
        if abs_sum > 0:
            for i in range(len(data)):
                data[i] = data[i] / abs_sum
        return data

    def start_new_epoch(self, learning_data):
        for row in learning_data:
            correct_answer = list(map(int, bin(row[0])[2:].rjust(4, '0')))
            input_data = row[1:]

            hidden_layer = [0 for _ in range(self.layers[1])]
            output_layer = [0 for _ in range(self.layers[2])]

            for i in range(len(hidden_layer)):
                hidden_layer[i] = self.weight_function(input_data, 0, i)
            for i in range(len(output_layer)):
                output_layer[i] = self.weight_function(hidden_layer, 1, i)

            output_mistake = [0 for _ in range(self.layers[2])]
            for i in range(self.layers[2]):
                output_mistake[i] = correct_answer[i] - output_layer[i]
            hidden_mistake = [0 for _ in range(self.layers[1])]
            for i in range(self.layers[1]):
                hidden_mistake[i] = sum([output_mistake[j] * self.weights[1][j][i] for j in range(len(output_mistake))])
            # hidden_mistake = self.normalize(hidden_mistake)

            for i in range(len(output_mistake)):
                self.correct_weights(1, i, hidden_layer, output_mistake[i])
            for i in range(len(hidden_mistake)):
                self.correct_weights(0, i, input_data, hidden_mistake[i])
        self.save_weights()

    def make_prediction(self, input_data):
        for i in range(len(self.layers) - 1):
            neurons = [0 for _ in range(self.layers[i + 1])]
            for j in range(len(neurons)):
                neurons[j] = self.weight_function(input_data, i, j)
            input_data = neurons.copy()
        ans = sum([input_data[i] * 2 ** (self.layers[-1] - i) for i in range(self.layers[-1])])
        return ans

    def validation_test(self, test_data):
        right_answers = 0
        total = len(test_data)
        for row in test_data:
            ans_exp = row[0]
            input_data = row[1:]
            ans_got = self.make_prediction(input_data)
            right_answers += ans_exp == ans_got
        print("Validation:", right_answers / total)

    def start_learning(self, epochs, training_data, validation_data):
        for i in range(epochs):
            t = time()
            self.start_new_epoch(training_data)
            self.validation_test(validation_data)
            print("Epoch", i, ":", (time() - t) / 60)
            print("----------------")
