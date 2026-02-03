import numpy as np
import matplotlib.pyplot


# Create array to store sensor values
backLegSensorValues = np.zeros(10000)

np.load('data/backLegSensorValues.npy')

print(backLegSensorValues)
