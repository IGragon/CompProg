from ML.RecognizeDigitsMNIST.Model import Model
import csv

model = Model(file_save="test_n1.txt", hidden_neurons=50)
train_data = []
test_data = []
with open("mnist_train.csv", 'r') as f:
    data = csv.reader(f)
    for row in data:
        train_data.append([int(row[0])] + model.normalize(list(map(float, row[1:]))))
    f.close()
with open("mnist_test.csv", 'r') as f:
    data = csv.reader(f)
    for row in data:
        test_data.append([int(row[0])] + model.normalize(list(map(float, row[1:]))))
    f.close()

model.start_learning(20, train_data, test_data)
