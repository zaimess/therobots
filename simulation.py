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
    def __init__(self, directOrGUI, solutionID):
        if directOrGUI == "DIRECT":
            self.physicsClient = p.connect(p.DIRECT)
        else:
            self.physicsClient = p.connect(p.GUI)

        p.setAdditionalSearchPath(pybullet_data.getDataPath())
        p.setGravity(0, 0, c.gravity)

        self.world = WORLD(solutionID)
        self.robot = ROBOT(solutionID)

    def run(self):
        for t in range(c.tstep):
            p.stepSimulation()
            self.robot.sense(t)
            self.robot.Think()
            self.robot.act(t)

            # IDK how this works..., but it does!\
            # Only slows sim speed if GUI
            if p.getConnectionInfo()['connectionMethod'] == p.GUI:
                time.sleep(1 / 60)

    def Get_Fitness(self, solutionID):
        self.robot.Get_Fitness(solutionID)

    def __del__(self):
        p.disconnect()
