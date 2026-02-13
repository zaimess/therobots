import pyrosim.pyrosim as pyrosim
import pybullet as p
import pybullet_data
import time
import numpy as np
import random

physicsClient = p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())

p.setGravity(0, 0, -9.8)
planeId = p.loadURDF("plane.urdf")
p.loadSDF("world.sdf")
robotId = p.loadURDF("body.urdf")
pyrosim.Prepare_To_Simulate(robotId)

# Create array to store sensor values
backLegSensorValues = np.zeros(1000)
frontLegSensorValues = np.zeros(1000)

# Motor control angle variables
BL_amplitude = np.pi / 4
BL_frequency = 8
BL_phastOffSset = 30

FL_amplitude = np.pi / 4
FL_frequency = 8
FL_phastOffSset = 0

# Create a vector to store sinusoidal values
x = np.linspace(0, 2 * np.pi, 1000)
BL_targetAngles = BL_amplitude*np.sin(BL_frequency*x + BL_phastOffSset)
# np.save("data/targetAngles.npy", targetAngles)
y = np.linspace(0, 2 * np.pi, 1000)
FL_targetAngles = FL_amplitude*np.sin(FL_frequency*y + FL_phastOffSset)

for i in range(1000):
    p.stepSimulation()

    # Store sensor values in respective vectors
    backLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
    frontLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("FrontLeg")

    # Back leg Motor
    pyrosim.Set_Motor_For_Joint(

        bodyIndex=robotId,

        jointName=b'Torso_BackLeg',

        controlMode=p.POSITION_CONTROL,

        targetPosition=BL_targetAngles[i],

        maxForce=500)

    # Front leg motor
    pyrosim.Set_Motor_For_Joint(

        bodyIndex=robotId,

        jointName=b'Torso_FrontLeg',

        controlMode=p.POSITION_CONTROL,

        targetPosition=FL_targetAngles[i],

        maxForce=500)

    time.sleep(1/60)

# Save sensor files to file
np.save("data/BackLegSensorValues.npy", backLegSensorValues)
np.save("data/FrontLegSensorValues.npy", frontLegSensorValues)

p.disconnect()
