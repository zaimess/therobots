import pyrosim.pyrosim as pyrosim


def create_world():
    pyrosim.Start_SDF("world.sdf")
    pyrosim.Send_Cube(name="Box", pos=[-4, 3, .5], size=[1, 1, 1])
    pyrosim.End()


# def create_robot():
#     pyrosim.Start_URDF("body.urdf")
#
#     pyrosim.Send_Cube(name="Link0", pos=[0, 0, .5], size=[1, 1, 1])
#     pyrosim.Send_Joint(name="Link0-Link1", parent="Link0", child="Link1",
#                        type="revolute", position=[0, 0, 1])
#     pyrosim.Send_Cube(name="Link1", pos=[0, 0, .5], size=[1, 1, 1])
#
#     pyrosim.Send_Joint(name="Link1-Link2", parent="Link1", child="Link2",
#                        type="revolute", position=[0, 0, 1])
#     pyrosim.Send_Cube(name="Link2", pos=[0, 0, .5], size=[1, 1, 1])
#
#     pyrosim.Send_Joint(name="Link2-Link3", parent="Link2", child="Link3",
#                        type="revolute", position=[.5, 0, .5])
#     pyrosim.Send_Cube(name="Link3", pos=[.5, 0, 0], size=[1, 1, 1])
#
#     pyrosim.Send_Joint(name="Link3-Link4", parent="Link3", child="Link4",
#                        type="revolute", position=[1, 0, 0])
#     pyrosim.Send_Cube(name="Link4", pos=[.5, 0, 0], size=[1, 1, 1])
#
#     pyrosim.Send_Joint(name="Link4-Link5", parent="Link4", child="Link5",
#                        type="revolute", position=[.5, 0, -.5])
#     pyrosim.Send_Cube(name="Link5", pos=[0, 0, -.5], size=[1, 1, 1])
#
#     pyrosim.Send_Joint(name="Link5-Link6", parent="Link5", child="Link6",
#                        type="revolute", position=[0, 0, -1])
#     pyrosim.Send_Cube(name="Link6", pos=[0, 0, -.5], size=[1, 1, 1])
#
#     pyrosim.Send_Joint(name="Link2-Link7", parent="Link2", child="Link7",
#                        type="revolute", position=[-.5, 0, 1])
#     pyrosim.Send_Cube(name="Link7", pos=[-0.5, 0, .5], size=[1, 1, 1])
#
#     pyrosim.End()

def create_robot():
    pyrosim.Start_URDF("body.urdf")
    pyrosim.Send_Cube(name="Torso", pos=[1.5, 0, 1.5], size=[1, 1, 1])
    pyrosim.Send_Joint(name="Torso-BackLeg", parent="Torso", child="BackLeg",
                       type="revolute", position=[1, 0, 1])
    pyrosim.Send_Cube(name="BackLeg", pos=[-.5, 0, -.5], size=[1, 1, 1])

    pyrosim.Send_Joint(name="Torso-FrontLeg", parent="Torso", child="FrontLeg",
                       type="revolute", position=[2, 0, 1])
    pyrosim.Send_Cube(name="FrontLeg", pos=[.5, 0, -.5], size=[1, 1, 1])

    pyrosim.End()


create_world()
create_robot()

