from solution import SOLUTION
import copy
import constants as c
import os
import numpy as np
import matplotlib.pyplot as plt


class PARALLEL_HILL_CLIMBER:
    def __init__(self):
        os.system("del brain*.nndf")
        os.system("del fitness[0-9]*.txt")
        os.system("del body*.urdf")
        os.system("del world*.sdf")

        self.parents = {}
        self.nextAvailableID = 0
        self.fitnessOverTime = []

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

        self.Plot_Fitness()

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
        self.Record_Fitness()
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

    def Record_Fitness(self):
        best = min(self.parents[k].fitness for k in self.parents)
        self.fitnessOverTime.append(best)

    def Plot_Fitness(self):
        label = "body_brain" if c.evolveBody else "brain_only"

        run = 1
        while os.path.exists(f"fitness_{label}_run{run}.txt"):
            run += 1

        np.savetxt(f"fitness_{label}_run{run}.txt", self.fitnessOverTime)

        plt.plot(self.fitnessOverTime, label=f"{label.replace('_', ' + ').title()} Run {run}")
        plt.xlabel("Generation")
        plt.ylabel("Best Fitness (x displacement)")
        plt.title("Fitness Over Generations")
        plt.legend()
        plt.tight_layout()
        plt.savefig(f"fitness_{label}_run{run}.png")
        plt.show()

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

    # def Show_Best(self):
    #     bestParent = 0
    #     for key in self.parents:
    #         if self.parents[key].fitness < self.parents[bestParent].fitness:
    #             bestParent = key
    #
    #     print(f"Best fitness: {self.parents[bestParent].fitness}")
    #     self.parents[bestParent].Start_Simulation("GUI")

    def Show_Best(self):
        bestParent = 0
        for key in self.parents:
            if self.parents[key].fitness < self.parents[bestParent].fitness:
                bestParent = key

        best = self.parents[bestParent]
        print(f"Best fitness: {best.fitness}")
        print(f"Best ID: {best.myID}")
        print(f"Best upper legs: {best.upperLegLength}")
        print(f"Best lower legs: {best.lowerLegLength}")
        best.Start_Simulation("GUI")
