from robodk import robolink

RDK = robolink.Robolink()


robot2 = RDK.Item('R2')
robot = RDK.Item('R1')
frame1 = RDK.Item('R1Base')
frame3 = RDK.Item('R2Base')
robot.setPoseFrame(frame1)


place= RDK.Item('R1Place')      # Defined relative to Table frame
preplace = RDK.Item('R1PrePlace')  # Defined relative to Conveyor frame  
home= RDK.Item('R1Home')   # Defined relative to Robot base

print("Moving to pick point on table...")
robot.MoveJ(home)

print("Moving to place point on conveyor...")
robot.MoveJ(preplace)

print("Returning home...")
robot.MoveL(place)

print("Moving to place point on conveyor...")
robot.MoveL(preplace)

print("Moving to pick point on table...")
robot.MoveJ(home)


frame2 = RDK.Item('SSFrameBrown')


pick= RDK.Item('SSBrownPick')      # Defined relative to Table frame
prepick = RDK.Item('SSBrownPrePick')

robot.setPoseFrame(frame2)

robot.MoveJ(prepick)
robot.MoveL(pick)

