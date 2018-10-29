
###################################### Python code for Case 3 #######################################


import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import fsolve
from scipy.integrate import odeint

# Initial values of v and w
v0 = [-0.25, 0.5, 0.5, 1.5]
w0 = [-0.1, 0.125, 0.2, 0.0]
I = 0.05
a = 0.5
b = 0.1
r = 1.1

# function for computing the integral values
def f(s,t):
	v = s[0]
	w = s[1]
	dvdt = v*(a-v)*(v-1) - w + I
	dwdt = b*v - r*w
	return [dvdt, dwdt]

v = np.linspace(-0.5, 1.75, 100)
	
w_dot = b*v/r
v_dot = v*(a-v)*(v-1) + I

idx = np.argwhere(np.diff(np.sign(w_dot - v_dot))).flatten()
labels = ["p1", "p2", "p3"]

# Plot of null clines
plt.figure(10)
plt.plot(v, v_dot, label=r'$\nu$ nullcline', color="b")
plt.plot(v, w_dot, label=r'$\omega$ nullcline', color="r")
plt.scatter(v[idx], v_dot[idx], label='Intersection', color="g")
for label, x, y in zip(labels, v[idx], v_dot[idx]):
    plt.annotate(
        label,
        xy=(x, y), xytext=(-20, 20),
        textcoords='offset points', ha='right', va='bottom',
        bbox=dict(boxstyle='round,pad=0.5', fc='yellow', alpha=0.5),
        arrowprops=dict(arrowstyle = '->', connectionstyle='arc3,rad=0'))
    print("\n{} : v = {}, w = {}".format(label, x, y))
plt.xlim((-0.5, 1.75))
plt.ylim((-0.2, 0.3))
plt.xlabel(r"$\nu$")
plt.ylabel(r'$\omega$')
plt.legend()
plt.title("Phase Plot")



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

	v = np.linspace(-0.5, 1.75, 1000)
	
	# v and w nullclines
	w_dot = b*v/r
	v_dot = v*(a-v)*(v-1) + I

	plt.figure(i+4)
	plt.plot(v, v_dot, label=r'$\nu$ nullcline', color="b")
	plt.plot(v, w_dot, label=r'$\omega$ nullcline', color="r")
	plt.plot(s[:,0], s[:,1], label="Trajectory", color="g")
	plt.xlim((-0.5, 1.5))
	plt.ylim((-0.3, 0.3))
	plt.xlabel(r"$\nu$")
	plt.ylabel(r'$\omega$')
	plt.legend()
	plt.title("Trajectory on the phase plane")


# Quiver plot for the trajectories at each point (v,w)
v = np.linspace(-0.5, 1.5, 20)
w = np.linspace(-0.2, 0.3, 20)

V, W = np.meshgrid(v,w)

# v and w nullclines
w_dot = b*v/r
v_dot = v*(a-v)*(v-1) + I

# derivatives : dv/dt and dw/dt
DV = V*(a-V)*(V-1) - W + I
DW = b*V - r*W

idx = np.argwhere(np.diff(np.sign(w_dot - v_dot))).flatten()

plt.figure(20)
Q = plt.quiver(V, W, DV, DW, width=1e-3)
plt.plot(v, v_dot, label=r'$\nu$ nullcline', color="b")
plt.plot(v, w_dot, label=r'$\omega$ nullcline', color="r")
plt.scatter(v[idx], v_dot[idx], label='Intersection', color="g")
for label, x, y in zip(labels, v[idx], v_dot[idx]):
    plt.annotate(
        label,
        xy=(x, y), xytext=(-20, 20),
        textcoords='offset points', ha='right', va='bottom',
        bbox=dict(boxstyle='round,pad=0.5', fc='yellow', alpha=0.5),
        arrowprops=dict(arrowstyle = '->', connectionstyle='arc3,rad=0'))
plt.xlim((-0.5, 1.5))
plt.ylim((-0.2, 0.3))
plt.xlabel(r"$\nu$")
plt.ylabel(r'$\omega$')
plt.legend()
plt.title("Trajectory on the phase plane")
plt.show()