# Computational-Neuroscience
Repository contains python as well as MATLAB codes used to get a better understanding about the functioning of network of neurons in the brain.

## 1. HH Model
Use simulated Hodgkin Huxley model and compute the following :

Threshold values for the external applied currents I1 , I2 , and I3 in which shift of dynamical behavior from one to another is seen, such as no AP, finite number of AP’s, Continuous firing and then followed by distortion resulting in no more APs is portrayed.

A graph which depicts the firing rate (frequency) as you change the applied external current ( i.e. Iext vs. Firing rate (f))


## 2. FitzHugh-Nagumo neuron model : Python
Simulation of FitzHugh-Nagumo neuron model for better understanding of the dynamics.

Note : Read report for usage of codes.

The model has been analysed for different values of external current.

The trajectories on the Phase plot as well as the behaviour around the nullclines have been demonstrated.

The stable points and limit cycle behaviour have been demonstrated.


## 3. CNN : MATLAB
The network comprises of a convolutional layer as well as a fully connected layer, used as a classifier for MNIST handwritten digits dataset.

Main code for training : "Traincnn.m".

The network is saved as CNN_Network.

"visualise.m" loads the saved network and saves the visualised filters as both grey scale and a colour map.

The analysis of the network, results and inferences can be found in "Report.pdf".

The dataset can be downloaded from : http://yann.lecun.com/exdb/mnist/

## 4. Hopfield Network
Developed code for Discrete Hopfield Network for storing single and multiple patterns (images). The stored patterns from the network are retrieved using the corresponding the input trigger. The input triggers, original pattern and retrieved patterns have been visualised.

Noise has been introduced into the strorage weights and its effects on pattern retreival analysed.
