
################### CODE TO VISUALISE THE TEXT FILES AS IMAGES ####################

import numpy as np
import scipy.misc

# Read the txt files
ball = np.genfromtxt("ball.txt", skip_header=-1, delimiter=",")
cat = np.genfromtxt("cat.txt", skip_header=-1, delimiter=",")
mona = np.genfromtxt("mona.txt", skip_header=-1, delimiter=",")

# The current scipy version started to normalize all images 
# so that min(data) become black and max(data) become white.
scipy.misc.imsave('ball.jpg', ball)
scipy.misc.imsave('cat.jpg', cat)
scipy.misc.imsave('mona.jpg', mona)
