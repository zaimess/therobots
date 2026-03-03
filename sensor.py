import pyrosim.pyrosim as pyrosim
import pybullet as p
import pybullet_data
import time
import numpy as np
import random
import constants as c


class SENSOR:
    def __init__(self, linkName):
        self.linkName = linkName
        self.values = np.zeros(c.tstep)

    def get_value(self, t):
        self.values[t] = pyrosim.Get_Touch_Sensor_Value_For_Link(self.linkName)

    def save_values(self, i):
        SensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link(self.linkName)
        np.save("data/FrontLegSensorValues.npy", frontLegSensorValues)

