
################## Python code for generating nullclines for v and w for I=0.1 #####################

import numpy as np
import matplotlib.pyplot as plt

I = 0.1
a = 0.5
b = 0.1
r = 0.1

v = np.linspace(-0.5, 1.5, 50)

w_dot = b*v/r
v_dot = v*(a-v)*(v-1) + I

plt.figure(0)
plt.plot(v, w_dot, color="r")
plt.xlabel(r"$\nu$")
plt.ylabel(r'$\omega$')
plt.xlim((-0.5, 1.5))
plt.ylim((-1, 1))
plt.title(r'$\omega$ nullcline')

plt.figure(1)
plt.plot(v, v_dot, color="b")
plt.xlabel(r"$\nu$")
plt.ylabel(r'$\omega$')
plt.xlim((-0.5, 1.5))
plt.ylim((-1, 1))
plt.title(r'$\nu$ nullcline')
plt.show()