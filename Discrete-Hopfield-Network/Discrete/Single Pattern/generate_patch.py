import numpy as np 
from matplotlib.image import imread
import scipy.misc

# Read the image
img = imread('../../ball.jpg')
img2 = np.genfromtxt("../../ball.txt", skip_header=-1, delimiter=",")
img2 = np.reshape(img2, (90,100))

# Initialise U as vector of 150 -  since max = 255, min =1, to get grey, put 150
U = np.ones_like(img)*150
U2 = np.zeros_like(img2)

############### Replace a random patch of U with a patch of image ###############
# Patch from [start_x:start_x + b, start_y:start_y + h]
start_x = int(np.random.uniform(0, 45))
start_y = int(np.random.uniform(0, 50))
b = int(np.random.uniform(5, 45))
h = int(np.random.uniform(15, 50))

# Generate the patch
U[start_x:start_x + b, start_y:start_y + h] = img[start_x:start_x + b, start_y:start_y + h]
U2[start_x:start_x + b, start_y:start_y + h] = img2[start_x:start_x + b, start_y:start_y + h]

# Save U
scipy.misc.imsave('ball_init.jpg', U)
np.savetxt("ball_init.txt", U2, delimiter=',')
