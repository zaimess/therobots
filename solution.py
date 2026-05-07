import numpy as np
import pyrosim.pyrosim as pyrosim
import os
import random
import time
import constants as c


class SOLUTION:
    def __init__(self, myID):
        self.weights = np.random.rand(c.numSensorNeurons, c.numMotorNeurons) * 2 - 1
        self.myID = myID

        if c.evolveBody:
            self.upperLegLength = 0.3 + np.random.rand(c.numUpperLegs) * 1.2
            self.lowerLegLength = 0.3 + np.random.rand(c.numLowerLegs) * 1.2
        else:
            self.upperLegLength = np.ones(c.numUpperLegs)
            self.lowerLegLength = np.ones(c.numLowerLegs)

    def Evaluate(self, directOrGUI):
        self.Create_World()
        self.Create_Body()
        self.Create_Brain()

    def Start_Simulation(self, directOrGUI):
        self.Create_World()
        self.Create_Body()
        self.Create_Brain()
        # os.system(f'start /B "" python simulate.py {directOrGUI} {self.myID} > NUL 2>&1')
        os.system(f'start /B "" python simulate.py {directOrGUI} {self.myID}')

    # def Wait_For_Simulation_To_End(self):
    #     fitnessFileName = f"fitness{self.myID}.txt"
    #
    #     while not os.path.exists(fitnessFileName):
    #         time.sleep(0.01)
    #
    #     with open(fitnessFileName, "r") as f:
    #         self.fitness = float(f.read())
    #
    #     os.system(f"del fitness{self.myID}.txt")

    def Wait_For_Simulation_To_End(self):
        fitnessFileName = f"fitness{self.myID}.txt"

        while not os.path.exists(fitnessFileName):
            time.sleep(0.01)

        # Retry loop to handle Windows file locking during rename
        for _ in range(50):  # up to 0.5 seconds of retries
            try:
                with open(fitnessFileName, "r") as f:
                    self.fitness = float(f.read())
                break
            except (PermissionError, ValueError):
                time.sleep(0.01)
        else:
            raise RuntimeError(f"Could not read {fitnessFileName} after retries")

        os.system(f"del fitness{self.myID}.txt")

    def Create_World(self):
        pyrosim.Start_SDF(f"world{self.myID}.sdf")
        # pyrosim.Send_Cube(name="Box", pos=[-4, 3, 0.5], size=[1, 1, 1])
        pyrosim.End()

    def Create_Body(self):
        pyrosim.Start_URDF(f"body{self.myID}.urdf")

        # Torso
        pyrosim.Send_Cube(name="Torso", pos=[0, 0, 1], size=[1, 1, 1])

        # ----------- BackLeg -------------
        # Hip joint at back edge of torso
        pyrosim.Send_Joint(
            name="Torso_BackLeg",
            parent="Torso",
            child="BackLeg",
            type="revolute",
            position=[0, -0.5, 1],
            jointAxis="1 0 0"
        )

        # Upper leg extends in negative y from the hip
        pyrosim.Send_Cube(
            name="BackLeg",
            pos=[0, -self.upperLegLength[0] / 2, 0],
            size=[0.2, self.upperLegLength[0], 0.2]
        )

        # Knee joint at end of upper leg
        pyrosim.Send_Joint(
            name="BackLeg_BackLowerLeg",
            parent="BackLeg",
            child="BackLowerLeg",
            type="revolute",
            position=[0, -self.upperLegLength[0], 0],
            jointAxis="1 0 0"
        )

        # Lower leg extends downward in z
        pyrosim.Send_Cube(
            name="BackLowerLeg",
            pos=[0, 0, -self.lowerLegLength[0] / 2],
            size=[0.2, 0.2, self.lowerLegLength[0]]
        )

        # ----------- FrontLeg -------------
        pyrosim.Send_Joint(
            name="Torso_FrontLeg",
            parent="Torso",
            child="FrontLeg",
            type="revolute",
            position=[0, 0.5, 1],
            jointAxis="1 0 0"
        )

        # Upper leg extends in positive y
        pyrosim.Send_Cube(
            name="FrontLeg",
            pos=[0, self.upperLegLength[1] / 2, 0],
            size=[0.2, self.upperLegLength[1], 0.2]
        )

        pyrosim.Send_Joint(
            name="FrontLeg_FrontLowerLeg",
            parent="FrontLeg",
            child="FrontLowerLeg",
            type="revolute",
            position=[0, self.upperLegLength[1], 0],
            jointAxis="1 0 0"
        )

        pyrosim.Send_Cube(
            name="FrontLowerLeg",
            pos=[0, 0, -self.lowerLegLength[1] / 2],
            size=[0.2, 0.2, self.lowerLegLength[1]]
        )

        # ----------- LeftLeg -------------
        pyrosim.Send_Joint(
            name="Torso_LeftLeg",
            parent="Torso",
            child="LeftLeg",
            type="revolute",
            position=[-0.5, 0, 1],
            jointAxis="0 1 0"
        )

        # Upper leg extends in negative x
        pyrosim.Send_Cube(
            name="LeftLeg",
            pos=[-self.upperLegLength[2] / 2, 0, 0],
            size=[self.upperLegLength[2], 0.2, 0.2]
        )

        pyrosim.Send_Joint(
            name="LeftLeg_LeftLowerLeg",
            parent="LeftLeg",
            child="LeftLowerLeg",
            type="revolute",
            position=[-self.upperLegLength[2], 0, 0],
            jointAxis="0 1 0"
        )

        pyrosim.Send_Cube(
            name="LeftLowerLeg",
            pos=[0, 0, -self.lowerLegLength[2] / 2],
            size=[0.2, 0.2, self.lowerLegLength[2]]
        )

        # ----------- RightLeg -------------
        pyrosim.Send_Joint(
            name="Torso_RightLeg",
            parent="Torso",
            child="RightLeg",
            type="revolute",
            position=[0.5, 0, 1],
            jointAxis="0 1 0"
        )

        # Upper leg extends in positive x
        pyrosim.Send_Cube(
            name="RightLeg",
            pos=[self.upperLegLength[3] / 2, 0, 0],
            size=[self.upperLegLength[3], 0.2, 0.2]
        )

        pyrosim.Send_Joint(
            name="RightLeg_RightLowerLeg",
            parent="RightLeg",
            child="RightLowerLeg",
            type="revolute",
            position=[self.upperLegLength[3], 0, 0],
            jointAxis="0 1 0"
        )

        pyrosim.Send_Cube(
            name="RightLowerLeg",
            pos=[0, 0, -self.lowerLegLength[3] / 2],
            size=[0.2, 0.2, self.lowerLegLength[3]]
        )

        pyrosim.End()

    def Create_Brain(self):
        pyrosim.Start_NeuralNetwork(f"brain{self.myID}.nndf")

        pyrosim.Send_Sensor_Neuron(name=0, linkName="Torso")
        pyrosim.Send_Sensor_Neuron(name=1, linkName="BackLowerLeg")
        pyrosim.Send_Sensor_Neuron(name=2, linkName="FrontLowerLeg")
        pyrosim.Send_Sensor_Neuron(name=3, linkName="LeftLowerLeg")
        pyrosim.Send_Sensor_Neuron(name=4, linkName="RightLowerLeg")

        pyrosim.Send_Motor_Neuron(name=5, jointName="Torso_BackLeg")
        pyrosim.Send_Motor_Neuron(name=6, jointName="Torso_FrontLeg")
        pyrosim.Send_Motor_Neuron(name=7, jointName="Torso_LeftLeg")
        pyrosim.Send_Motor_Neuron(name=8, jointName="Torso_RightLeg")

        pyrosim.Send_Motor_Neuron(name=9, jointName="BackLeg_BackLowerLeg")
        pyrosim.Send_Motor_Neuron(name=10, jointName="FrontLeg_FrontLowerLeg")
        pyrosim.Send_Motor_Neuron(name=11, jointName="LeftLeg_LeftLowerLeg")
        pyrosim.Send_Motor_Neuron(name=12, jointName="RightLeg_RightLowerLeg")

        for currentRow in range(c.numSensorNeurons):
            for currentColumn in range(c.numMotorNeurons):
                pyrosim.Send_Synapse(
                    sourceNeuronName=currentRow,
                    targetNeuronName=currentColumn + c.numSensorNeurons,
                    weight=self.weights[currentRow][currentColumn]
                )

        pyrosim.End()

    def Mutate(self):
        randomRow = random.randint(0, c.numSensorNeurons - 1)
        randomColumn = random.randint(0, c.numMotorNeurons - 1)

        self.weights[randomRow, randomColumn] = random.random() * 2 - 1

        if c.evolveBody:
            randomUpperLeg = random.randint(0, c.numUpperLegs - 1)
            randomLowerLeg = random.randint(0, c.numLowerLegs - 1)

            self.upperLegLength[randomUpperLeg] = 0.3 + random.random() * 1.2
            self.lowerLegLength[randomLowerLeg] = 0.3 + random.random() * 1.2

    def Set_ID(self, myID):
        self.myID = myID
