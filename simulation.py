import pyrosim.pyrosim as pyrosim
import pybullet as p
import pybullet_data
import time
import numpy as np
import random
import constants as c
from world import WORLD
from robot import ROBOT


class SIMULATION:
    def __init__(self):
        self.physicsClient = p.connect(p.GUI)
        p.setAdditionalSearchPath(pybullet_data.getDataPath())
        p.setGravity(0, 0, c.gravity)

        self.world = WORLD()
        self.robot = ROBOT()

    def run(self):
        for t in range(c.tstep):
            p.stepSimulation()
            self.robot.sense(t)
            self.robot.act(t)

            time.sleep(1/60)

    def __del__(self):
        p.disconnect()
