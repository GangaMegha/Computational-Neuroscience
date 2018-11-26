import numpy as np 
from matplotlib.image import imread
import scipy.misc

######################### Read the image #########################
# Ball
img1 = imread('../../ball.jpg')
img1_ = np.genfromtxt("../../ball.txt", skip_header=-1, delimiter=",")
img1_ = np.reshape(img1_, (90,100))

# Cat
img2 = imread('../../cat.jpg')
img2_ = np.genfromtxt("../../cat.txt", skip_header=-1, delimiter=",")
img2_ = np.reshape(img2_, (90,100))

# Monalisa
img3 = imread('../../mona.jpg')
img3_ = np.genfromtxt("../../mona.txt", skip_header=-1, delimiter=",")
img3_ = np.reshape(img3_, (90,100))

############## Initialise U as vector of 150 -  since max = 255, min =1, to get grey, put 150 #################
# Ball
U1 = np.ones_like(img1)*150
U1_ = np.zeros_like(img1_)

# Cat
U2 = np.ones_like(img2)*150
U2_ = np.zeros_like(img2_)

# Monalisa
U3 = np.ones_like(img3)*150
U3_ = np.zeros_like(img3_)

############### Replace a random patch of U with a patch of image ###############
# Patch from [start_x:start_x + b, start_y:start_y + h]

# Ball
start_x1 = int(np.random.uniform(0, 45))
start_y1 = int(np.random.uniform(0, 50))
b1 = int(np.random.uniform(5, 45))
h1 = int(np.random.uniform(15, 50))

# Cat
start_x2 = int(np.random.uniform(0, 45))
start_y2 = int(np.random.uniform(0, 50))
b2 = int(np.random.uniform(5, 45))
h2 = int(np.random.uniform(15, 50))

# Monalisa
start_x3 = int(np.random.uniform(0, 45))
start_y3 = int(np.random.uniform(0, 50))
b3 = int(np.random.uniform(5, 45))
h3 = int(np.random.uniform(15, 50))

#################### Generate the patch #######################
# Ball
U1[start_x1:start_x1 + b1, start_y1:start_y1 + h1] = img1[start_x1:start_x1 + b1, start_y1:start_y1 + h1]
U1_[start_x1:start_x1 + b1, start_y1:start_y1 + h1] = img1_[start_x1:start_x1 + b1, start_y1:start_y1 + h1]

# Cat
U2[start_x2:start_x2 + b2, start_y2:start_y2 + h2] = img2[start_x2:start_x2 + b2, start_y2:start_y2 + h2]
U2_[start_x2:start_x2 + b2, start_y2:start_y2 + h2] = img2_[start_x2:start_x2 + b2, start_y2:start_y2 + h2]

# Monalisa
U3[start_x3:start_x3 + b3, start_y3:start_y3 + h3] = img3[start_x3:start_x3 + b3, start_y3:start_y3 + h3]
U3_[start_x3:start_x3 + b3, start_y3:start_y3 + h3] = img3_[start_x3:start_x3 + b3, start_y3:start_y3 + h3]

######################## Save U ###############################
# Ball
scipy.misc.imsave('ball_init_noise.jpg', U1)
np.savetxt("ball_init_noise.txt", U1_, delimiter=',')

# Cat
scipy.misc.imsave('cat_init_noise.jpg', U2)
np.savetxt("cat_init_noise.txt", U2_, delimiter=',')

# Monalisa
scipy.misc.imsave('mona_init_noise.jpg', U3)
np.savetxt("mona_init_noise.txt", U3_, delimiter=',')