import numpy as np
from random import randint, random, choice, uniform
from PIL import Image, ImageDraw
from matplotlib import pyplot as plt
from matplotlib.animation import FuncAnimation

fig = plt.figure()
ax = plt.axes(xlim=(-105, 105), ylim=(-105, 105))
line, = ax.plot([], [], 'bo', markersize=3)
line2, = ax.plot([], [], color='red')
n = 1000
n_frames = 300


def t(x, y):
    return sum([(x - a[i][0]) ** 2 + (y - a[i][1]) ** 2 for i in range(len_a)])


def next_iteration():
    next_gen = [0] * n
    for i in range(n):
        x = choice(b)[0] + uniform(-0.1, 0.1)
        y = choice(b)[1] + uniform(-0.1, 0.1)
        next_gen[i] = [x, y, t(x, y)]
    return next_gen


def init():
    line.set_data([], [])
    line2.set_data([j[0] for j in a + a[0:1]], [j[1] for j in a + a[0:1]])
    return line, line2,


def animate(i):
    global b
    x = [j[0] for j in b]
    y = [j[1] for j in b]
    line.set_data(x, y)
    b = sorted(b, key=lambda x: x[2])[:int(n * 0.95)]
    b = next_iteration()
    if i == n_frames - 1:
        avg_x = sum(b[j][0] for j in range(n)) / n
        avg_y = sum(b[j][1] for j in range(n)) / n
        print(avg_x, avg_y)
    return line, line2,


# a = [(-100, -10), (-80, 40), (-10, 60), (10, 100), (100, 20), (60, 0), (20, -100), (-90, -70), (-60, -30)]
a = [(-100, -100), (-100, 100), (100, 100), (100, -100)]
# a = [(-100, 40), (-40, 20), (-50, 100), (20, 70), (50, 100), (100, 70), (60, 0), (100, -50), (50, -60), (-20, -100), (0, -40), (-70, -30)]
len_a = len(a)


b = [[randint(-100, 100), randint(-100, 100), 0] for _ in range(n)]
for i in range(n):
    b[i][2] = t(b[i][0], b[i][1])

b_dist = [b[i][2] for i in range(n)]


anim = FuncAnimation(fig, animate, init_func=init, frames=n_frames, interval=100)
anim.save('test_square_shape.gif', writer='imagemagick')
