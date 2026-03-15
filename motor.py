import pyrosim.pyrosim as pyrosim
import pybullet as p
import pybullet_data
import time
import numpy as np
import random
import constants as c


class MOTOR:
    def __init__(self, jointName):
        self.jointName = jointName

    def set_value(self, robot, desiredAngle):

        pyrosim.Set_Motor_For_Joint(

            bodyIndex=robot.robotId,

            jointName=self.jointName,

            controlMode=p.POSITION_CONTROL,

            targetPosition=desiredAngle,

            maxForce=c.mforce)

    def act(self):
        pass



