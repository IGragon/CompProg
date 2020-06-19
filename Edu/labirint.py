import pprint
from PIL import Image, ImageDraw
import matplotlib.pyplot as plt


def make(matrix):
    pass

n = 100
matrix = [[0] * n] * n
row_walls = [[1] * (n - 1)] * (n - 1)
col_walls = [[1] * (n - 1)] * (n - 1)

image = Image.new("RGB", (n, n), 'white')
plt.imshow(image)
