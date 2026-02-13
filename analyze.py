import numpy as np
import matplotlib.pyplot as m


# # Create array to store sensor values
# backLegSensorValues = np.load("data/BackLegSensorValues.npy")
# frontLegSensorValues = np.load("data/FrontLegSensorValues.npy")
#
#
# m.plot(backLegSensorValues, label='Back Leg Sensor Values', linewidth=3)
# m.plot(frontLegSensorValues, label='Front Leg Sensor Values')
# m.legend()
# m.show()

# Create array to store sinusoid values
targetAngles = np.load("data/targetAngles.npy")

m.plot(targetAngles, label='Target Angles')
m.legend()
m.show()
