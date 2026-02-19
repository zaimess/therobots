import numpy as np
import matplotlib.pyplot as m


# Create array to store sinusoid values
targetAngles = np.load("data/targetAngles.npy")

m.plot(targetAngles, label='Target Angles')
m.legend()
m.show()
