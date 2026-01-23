import pyrosim.pyrosim as pyrosim

pyrosim.Start_SDF("boxs.sdf")
# pyrosim.Send_Cube(name="Box", pos=[0,0,1.5] , size=[1,2,3])
# pyrosim.Send_Cube(name="Box2", pos=[0,0,.5] , size=[1,1,1])


def oneblocktower(row, col):
    for i in range(10):
        z = i
        s = .9 ** i
        pyrosim.Send_Cube(name="Box", pos=[row, col, .5 + z], size=[s, s, s])


for p in range(5):
    for j in range(5):
        oneblocktower(j, p)

pyrosim.End()

