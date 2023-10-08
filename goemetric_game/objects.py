import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

class Canvas:

    def __init__(self, height, width, r, g, b):
        self.width = width
        self.height = height
        self.r = int(r)
        self.g = int(g)
        self.b = int(b)
        data = np.zeros((self.height, self.width, 3), dtype=np.uint8)
        data[:] = [self.r, self.g, self.b]
        self.data = data

class Rectangle:

    def __init__(self, start_x, start_y, length, breath, r, g, b):
        self.breath = breath
        self.length = length
        self.start_y = start_y
        self.start_x = start_x
        self.r = int(r)
        self.g = int(g)
        self.b = int(b)

    def draw(self, canvas):
        canvas.data[self.start_x:self.start_x+self.length, self.start_y:self.start_y+ self.breath] = [self.r, self.g, self.b]




my_canvas = Canvas(10, 15, 253, 240, 240)
print(my_canvas.data)

my_rectangle = Rectangle(3, 5, 2, 3, 31, 65, 114)
my_rectangle.draw(my_canvas)


img = Image.fromarray(my_canvas.data)
plt.imshow(img)
plt.show()