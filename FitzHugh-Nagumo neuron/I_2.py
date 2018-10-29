
###################################### Python code for Case 3 #######################################


import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

# Initial values of v and w
w0 = [0.0, 1.5, 0.5, 1]
v0 = [0.0, 0.3, 0.7, 1.0]
I = 1.4
a = 0.5
b = 0.1
r = 0.1

# function for computing the integral values
def f(s,t):
	v = s[0]
	w = s[1]
	dvdt = v*(a-v)*(v-1) - w + I
	dwdt = b*v - r*w
	return [dvdt, dwdt]

t = np.linspace(0,100, 1000)

for i in range(4) :
	init=[v0[i],w0[i]]

	# array of values for v and w computed via integration
	s = odeint(f,init,t)


	plt.figure(i)
	plt.plot(t, s[:,1], label=r'$\omega$', color="r")
	plt.plot(t, s[:,0], label=r'$\nu$ ', color="b")
	plt.xlabel("t")
	plt.legend()
	plt.title("Variation w.r.t time")

	v = np.linspace(-0.5, 1.75, 100)
	
	# v and w nullclines
	w_dot = b*v/r
	v_dot = v*(a-v)*(v-1) + I

	plt.figure(i+4)
	plt.plot(v, v_dot, label=r'$\nu$ nullcline', color="b")
	plt.plot(v, w_dot, label=r'$\omega$ nullcline', color="r")
	plt.plot(s[:,0], s[:,1], label="Trajectory", color="g")
	plt.xlim((-0.5, 1.75))
	plt.xlabel(r"$\nu$")
	plt.ylabel(r'$\omega$')
	plt.legend()
	plt.title("Trajectory on the phase plane")
	plt.show()

# Quiver plot for the trajectories at each point (v,w)
v = np.linspace(-0.5, 1.5, 20)
w = np.linspace(0.5, 2.5, 20)

V, W = np.meshgrid(v,w)

# v and w nullclines
w_dot = b*v/r
v_dot = v*(a-v)*(v-1) + I

# derivatives : dv/dt and dw/dt
DV = V*(a-V)*(V-1) - W + I
DW = b*V - r*W

plt.figure(19)
plt.plot(v, v_dot, label=r'$\nu$ nullcline', color="b")
plt.plot(v, w_dot, label=r'$\omega$ nullcline', color="r")
plt.xlim((-0.5, 1.5))
plt.ylim((0.5, 2.5))
plt.xlabel(r"$\nu$")
plt.ylabel(r'$\omega$')
plt.legend()
plt.title("Nullclines")

# Plot of null clines
plt.figure(20)
Q = plt.quiver(V, W, DV, DW, width=1e-3)
plt.plot(v, v_dot, label=r'$\nu$ nullcline', color="b")
plt.plot(v, w_dot, label=r'$\omega$ nullcline', color="r")
plt.xlim((-0.5, 1.5))
plt.ylim((0.5, 2.5))
plt.xlabel(r"$\nu$")
plt.ylabel(r'$\omega$')
plt.legend()
plt.title("Trajectory on the phase plane")
plt.show()