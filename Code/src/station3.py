from robodk import robolink

def station3(obj_to_attach_to, increment, iteration):
    RDK = robolink.Robolink()

    R7Tool = RDK.Item('R7Tool')
    R9Tool = RDK.Item('R9Tool')

    R7 = RDK.Item('R7')
    R8 = RDK.Item('R8')
    R9 = RDK.Item('R9')
    R10 = RDK.Item('R10')

    R7Base = RDK.Item('R7Base')
    R9Base = RDK.Item('R9Base')

    W1 = RDK.Item(f'W1_{increment}')
    W2 = RDK.Item(f'W2_{increment}')
    W3 = RDK.Item(f'W3_{increment}')
    W4 = RDK.Item(f'W4_{increment}')

    #R7 Points
    R7Home = RDK.Item('R7Home')
    RightWheelPlace = RDK.Item('RightWheelPlace')
    RightWheelPrePlace = RDK.Item('RightWheelPrePlace')
    RightWheelPick = RDK.Item('RightWheelPick')
    RightWheelPrePick = RDK.Item('RightWheelPrePick')

    #R9 Points
    R9Home = RDK.Item('R9Home')
    LeftWheelPlace = RDK.Item('LeftWheelPlace')
    LeftWheelPrePlace = RDK.Item('LeftWheelPrePlace')
    LeftWheelPick = RDK.Item('LeftWheelPick')
    LeftWheelPrePick = RDK.Item('LeftWheelPrePick')

    #Move Home
    R7.setPoseFrame(R7Base)
    R9.setPoseFrame(R9Base)

    R7.MoveJ(R7Home, blocking=False)
    R9.MoveJ(R9Home, blocking=False)

    R7.MoveJ(RightWheelPrePick, blocking=False)
    R9.MoveJ(LeftWheelPrePick, blocking=False)

    R7.MoveL(RightWheelPick, blocking=False)
    R9.MoveL(LeftWheelPick, blocking=False)

    while R7.Busy() or R9.Busy():
            a = 1

    #TODO ATTACH
    if iteration == 1:
        pose_abs = W1.PoseAbs()
        W1.setParent(R7Tool)
        W1.setPoseAbs(pose_abs)

        pose_abs = W2.PoseAbs()
        W2.setParent(R9Tool)
        W2.setPoseAbs(pose_abs)

    if iteration == 2:
        pose_abs = W3.PoseAbs()
        W3.setParent(R7Tool)
        W3.setPoseAbs(pose_abs)

        pose_abs = W4.PoseAbs()
        W4.setParent(R9Tool)
        W4.setPoseAbs(pose_abs)


    R7.MoveL(RightWheelPrePick, blocking=False)
    R9.MoveL(LeftWheelPrePick, blocking=False)

    R7.MoveJ(R7Home, blocking=False)
    R9.MoveJ(R9Home, blocking=False)

    R7.MoveJ(RightWheelPrePlace, blocking=False)
    R9.MoveJ(LeftWheelPrePlace, blocking=False)

    R7.MoveJ(RightWheelPlace, blocking=False)
    R9.MoveJ(LeftWheelPlace, blocking=False)

    R7.MoveJ(RightWheelPlace, blocking=False)
    R9.MoveJ(LeftWheelPlace, blocking=False)

    while R7.Busy() or R9.Busy():
            a = 1

    if iteration == 1:
        pose_abs = W1.PoseAbs()
        W1.setParent(obj_to_attach_to)
        W1.setPoseAbs(pose_abs)

        pose_abs = W2.PoseAbs()
        W2.setParent(obj_to_attach_to)
        W2.setPoseAbs(pose_abs)

    if iteration == 2:
        pose_abs = W3.PoseAbs()
        W3.setParent(obj_to_attach_to)
        W3.setPoseAbs(pose_abs)

        pose_abs = W4.PoseAbs()
        W4.setParent(obj_to_attach_to)
        W4.setPoseAbs(pose_abs)

    R7.MoveJ(R7Home, blocking=False)
    R9.MoveJ(R9Home, blocking=False)
