
##################### Python code for finding I1 and I2 values #######################

import numpy as np 
import matplotlib.pyplot as plt
from scipy.signal import argrelextrema

I = 0.0
a = 0.5
b = 0.1
r = 0.1
  
v = np.linspace(-0.5, 1.5, 50)
    
v_dot = v*(a-v)*(v-1) 

# local minima of v-nullcline 
local_min = argrelextrema(v_dot, np.less)[0]
# local maxima of v-nullcline
local_max = argrelextrema(v_dot, np.greater)[0]
print("\n\nIndex of local min and max : {}, {}".format(local_min-1, local_max))

# Values of I1 and I2 corresponding to local minima and maxima of v-nullcline respectively
I1 = 0 - v[local_min-1]*(a-v[local_min-1])*(v[local_min-1]-1) + b*v[local_min-1]/r
I2 = 0 - v[local_max]*(a-v[local_max])*(v[local_max]-1) + b*v[local_max]/r
print("\n\n I_1 = {}, \t I_2 = {}".format(I1, I2))

# v and w nullclines
w_dot = b*v/r
v_dot = v*(a-v)*(v-1) + I1

plt.figure(0)
plt.plot(v, v_dot, label=r'$\nu$ nullcline', color="b")
plt.plot(v, w_dot, label=r'$\omega$ nullcline', color="r")
plt.xlim((-0.5, 1.5))
plt.ylim((-1, 2))
plt.xlabel(r"$\nu$")
plt.ylabel(r'$\omega$')
plt.legend()
plt.title("Phase Plot for I1")

w_dot = b*v/r
v_dot = v*(a-v)*(v-1) + I2

plt.figure(1)
plt.plot(v, v_dot, label=r'$\nu$ nullcline', color="b")
plt.plot(v, w_dot, label=r'$\omega$ nullcline', color="r")
plt.xlim((-0.5, 1.5))
plt.ylim((-1, 2))
plt.xlabel(r"$\nu$")
plt.ylabel(r'$\omega$')
plt.legend()
plt.title("Phase Plot for I2")
plt.show()