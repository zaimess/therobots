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
        # self.prepare_to_act()

    # def prepare_to_act(self):
    #     self.amplitude = c.amplitude
    #     self.frequency = c.frequency
    #     self.offset = c.phaseOffSet
    #
    #     # Make one motor half frequency
    #     if self.jointName == b'Torso_BackLeg':
    #         self.frequency *= 0.5
    #
    #     x = np.linspace(0, 2 * np.pi, c.tstep)
    #     self.motorValues = self.amplitude * np.sin(self.frequency * x + self.offset)

    def set_value(self, robot, desiredAngle):

        pyrosim.Set_Motor_For_Joint(

            bodyIndex=robot.robotId,

            jointName=self.jointName,

            controlMode=p.POSITION_CONTROL,

            targetPosition=desiredAngle,

            maxForce=c.mforce)

    def act(self):
        pass



