import numpy as np 
from matplotlib.image import imread
import matplotlib.pyplot as plt
import scipy.misc

# No. of neurons
N = 9000
# No. of iterations
n_iter_sync = 5
n_iter_async = 100000


def Synchronous(V, W, img, filename):  # Batch update
	rmse = []
	for i in range(n_iter_sync):
		rmse.append(np.linalg.norm(img - V) / np.sqrt(N))
		V = np.sign(np.matmul(V, W))

	plt.figure(0)
	plt.clf()
	plt.plot(rmse)
	plt.xlabel("Iterations")
	plt.ylabel("RMSE")
	plt.title("RMSE Plot for Synchronous Update")
	plt.grid()
	plt.savefig("Sync_Plot_{}.png".format(filename))
	# plt.show()

	scipy.misc.imsave('Sync_reconstruct_{}.png'.format(filename), np.reshape(V*255/2+255/2, (90,100)))

def Asynchronous(V, W, img, filename): # Random point selected and updated
	rmse = []
	for i in range(n_iter_async):
		rmse.append(np.linalg.norm(img - V) / np.sqrt(N))
		indx = int(np.random.uniform(0,9000))
		V[0][indx] = np.sign(np.matmul(V, W[:,indx]))

	plt.figure(1)
	plt.clf()
	plt.plot(rmse)
	plt.xlabel("Iterations")
	plt.ylabel("RMSE")
	plt.title("RMSE Plot for Aynchronous Update")
	plt.grid()
	plt.savefig("Async_Plot_{}.png".format(filename))
	# plt.show()

	scipy.misc.imsave('Async_reconstruct_{}.png'.format(filename), np.reshape(V*255/2+255/2, (90,100)))

################### Read the images ####################
# Ball
img1 = np.genfromtxt("../../ball.txt", skip_header=-1, delimiter=",")
img1 = np.reshape(img1, (1,9000))

# Cat
img2 = np.genfromtxt("../../cat.txt", skip_header=-1, delimiter=",")
img2 = np.reshape(img2, (1,9000))

# Monalisa
img3 = np.genfromtxt("../../mona.txt", skip_header=-1, delimiter=",")
img3 = np.reshape(img3, (1,9000))

#################### Initial values as patches ################
# Ball
V1 = np.genfromtxt("ball_init_noise.txt", skip_header=-1, delimiter=",")
V1 = np.reshape(V1, (1,9000))

# Cat
V2 = np.genfromtxt("cat_init_noise.txt", skip_header=-1, delimiter=",")
V2 = np.reshape(V2, (1,9000))

# Monalisa
V3 = np.genfromtxt("mona_init_noise.txt", skip_header=-1, delimiter=",")
V3 = np.reshape(V3, (1,9000))


for X in [0.25, 0.50, 0.80] :

	####################### Initialise the weight matrix ################
	W = (1.0/N)*(	np.matmul(np.transpose(img1), img1) + 
					np.matmul(np.transpose(img2), img2) +
					np.matmul(np.transpose(img3), img3)
				)
	X_val = int(X*N*N)
	mask = np.hstack(( np.ones((1, int(N*N-X_val))) , np.zeros((1,X_val)) ))  
	mask = np.reshape(mask[0][np.random.permutation(N*N)], [N,N]) 

	W = W*mask

	################### Synchronous updates ######################
	# Ball
	Synchronous(V1, W, img1, "ball_noise_{}".format(X*100))

	# Cat
	Synchronous(V2, W, img2, "cat_noise_{}".format(X*100))

	# Monalisa
	Synchronous(V3, W, img3, "mona_noise_{}".format(X*100))

	################### Asynchronous updates #####################
	# Ball
	Asynchronous(V1, W, img1, "ball_noise_{}".format(X*100))

	# Cat
	Asynchronous(V2, W, img2, "cat_noise_{}".format(X*100))

	# Monalisa
	Asynchronous(V3, W, img3, "mona_noise_{}".format(X*100))


