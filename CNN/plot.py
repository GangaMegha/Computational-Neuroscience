# Code for plotting a 3D plot to evaluate variation of accuracy and training time with
# change in the No. of Filters, Filter Size and No. of Epochs
# Note : Values manually inserted after evaluation using "Traincnn_loop.m"

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
from matplotlib import cm

fig = plt.figure()
ax = fig.gca(projection='3d')

x1 = [16, 16, 16]
x2 = [25, 25, 25]
x3 = [36, 36, 36]
y1 = [3, 5, 11]


z1 = [17.39, 15.21, 9.34]
z2 = [27.03, 23.57, 14.36]
z3 = [38.78, 33.40, 20.5]
surf1 = ax.scatter(x1, y1, z1, 'r')
surf2 = ax.scatter(x2, y1, z2, 'g')
surf3 = ax.scatter(x3, y1, z3, 'b')
ax.set_xlabel("No. of filters")
ax.set_ylabel("Filter Dimension")
# ax.set_zlabel("Accuracy in %")
ax.set_zlabel("Training time (s)")
plt.title("No. of epochs = 20")

plt.show()

