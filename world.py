import pyrosim.pyrosim as pyrosim
import pybullet as p
import pybullet_data
import time
import numpy as np
import random
import os


class WORLD:
    def __init__(self, solutionID):
        self.planeId = p.loadURDF("plane.urdf")
        p.loadSDF(f"world{solutionID}.sdf")
        os.system(f"del world{solutionID}.sdf")

