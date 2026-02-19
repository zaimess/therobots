import pyrosim.pyrosim as pyrosim
import pybullet as p
import pybullet_data
import time
import numpy as np
import random


class WORLD:
    def __init__(self):
        self.planeId = p.loadURDF("plane.urdf")
        p.loadSDF("world.sdf")

