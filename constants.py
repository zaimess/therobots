import numpy as np

# Gravity
gravity = -32.2

# time step
tstep = 1000

# Actual motor control angle variables...?
amplitude = np.pi / 4
frequency = 10
phaseOffSet = 0

# Motor control angle variables
BL_amplitude = np.pi / 4
BL_frequency = 8
BL_phastOffSset = 30

FL_amplitude = np.pi / 4
FL_frequency = 8
FL_phastOffSset = 0

# Motor force value
mforce = 500

# Number of Generations
numberOfGenerations = 5

# Population Size
populationSize = 5

# Neuron Amounts
numSensorNeurons = 4
numMotorNeurons = 8

# Motor Joint Range
motorJointRange = .4
