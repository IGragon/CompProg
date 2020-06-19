import matplotlib.pyplot as plt
from random import random

f = [10] * 100

for i in range(1, 100):
    f[i - 1] = f[i] + random()

plt.plot(f, 'o')

plt.show()
