import numpy as np 
from matplotlib.image import imread
import matplotlib.pyplot as plt
import scipy.misc

# No. of neurons
N = 9000
# No. of iterations
n_iter_sync = 5
n_iter_async = 100000


def Synchronous(V, W, img):  # Batch update
	rmse = []
	for i in range(n_iter_sync):
		rmse.append(np.linalg.norm(img - V) / np.sqrt(N))
		V = np.sign(np.matmul(V, W))

	plt.figure(0)
	plt.plot(rmse)
	plt.xlabel("Iterations")
	plt.ylabel("RMSE")
	plt.title("RMSE Plot for Synchronous Update")
	plt.grid()
	plt.savefig("Sync_Plot_4.png")
	plt.show()

	scipy.misc.imsave('Sync_ball_reconstruct_4.png', np.reshape(V*255/2+255/2, (90,100)))

def Asynchronous(V, W, img): # Random point selected and updated
	rmse = []
	for i in range(n_iter_async):
		rmse.append(np.linalg.norm(img - V) / np.sqrt(N))
		indx = int(np.random.uniform(0,9000))
		V[0][indx] = np.sign(np.matmul(V, W[:,indx]))

	plt.figure(0)
	plt.plot(rmse)
	plt.xlabel("Iterations")
	plt.ylabel("RMSE")
	plt.title("RMSE Plot for Aynchronous Update")
	plt.grid()
	plt.savefig("Async_Plot_4.png")
	plt.show()

	scipy.misc.imsave('Async_ball_reconstruct_4.png', np.reshape(V*255/2+255/2, (90,100)))

# Read the image
img = np.genfromtxt("../../ball.txt", skip_header=-1, delimiter=",")
img = np.reshape(img, (1,9000))
V = np.genfromtxt("ball_init4.txt", skip_header=-1, delimiter=",")
V = np.reshape(V, (1,9000))

# Initialise the weight matrix
W = (1.0/N)*np.matmul(np.transpose(img), img)

# Synchronous updates
Synchronous(V, W, img)

# Asynchronous updates
Asynchronous(V, W, img)


