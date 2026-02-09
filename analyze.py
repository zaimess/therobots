import numpy as np
import matplotlib.pyplot as m


# Create array to store sensor values
backLegSensorValues = np.load("data/BackLegSensorValues.npy")
frontLegSensorValues = np.load("data/FrontLegSensorValues.npy")


m.plot(backLegSensorValues, label='Back Leg Sensor Values', linewidth=3)
m.plot(frontLegSensorValues, label='Front Leg Sensor Values')
m.legend()
m.show()
