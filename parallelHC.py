from solution import SOLUTION
import copy
import constants as c
import os


class PARALLEL_HILL_CLIMBER:
    def __init__(self):
        os.system("del brain*.nndf")
        os.system("del fitness*.txt")
        os.system("del body*.urdf")

        self.parents = {}
        self.nextAvailableID = 0

        for i in range(c.populationSize):
            self.parents[i] = SOLUTION(self.nextAvailableID)
            self.nextAvailableID += 1

    def Evolve(self):
        self.Evaluate(self.parents)

        print("Showing initial best robot...")
        self.Show_Best()
        input("Close the GUI window, then press Enter to begin evolution...")

        for currentGeneration in range(c.numberOfGenerations):
            print("Generation", currentGeneration)
            self.Evolve_For_One_Generation()

        print("Showing final best robot...")
        self.Show_Best()
        input("Close the GUI window, then press Enter to finish...")

    def Evaluate(self, solutions):
        for i in solutions:
            solutions[i].Start_Simulation("DIRECT")

        for i in solutions:
            solutions[i].Wait_For_Simulation_To_End()

    def Evolve_For_One_Generation(self):
        self.Spawn()
        self.Mutate()
        self.Evaluate(self.children)
        self.Select()
        self.Print()

    def Spawn(self):
        self.children = {}
        for i in self.parents:
            self.children[i] = copy.deepcopy(self.parents[i])
            self.children[i].Set_ID(self.nextAvailableID)
            self.nextAvailableID += 1

    def Mutate(self):
        for i in self.children:
            self.children[i].Mutate()

    def Select(self):
        for key in self.parents:
            if self.children[key].fitness < self.parents[key].fitness:
                self.parents[key] = self.children[key]

    def Print(self):
        print()
        for key in self.parents:
            print(
                "parent fitness:", self.parents[key].fitness,
                "child fitness:", self.children[key].fitness,
                "parent upper:", self.parents[key].upperLegLength,
                "child upper:", self.children[key].upperLegLength,
                "parent lower:", self.parents[key].lowerLegLength,
                "child lower:", self.children[key].lowerLegLength
            )
        print()

    def Show_Best(self):
        bestParent = 0

        for key in self.parents:
            if self.parents[key].fitness < self.parents[bestParent].fitness:
                bestParent = key

        self.parents[bestParent].Start_Simulation("GUI")
