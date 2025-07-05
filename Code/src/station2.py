from robodk import robolink

def station2(color):
    RDK = robolink.Robolink()

    CarBase = RDK.Item("Car_Base")

    R5Tool = RDK.Item('R5Tool')
    R6Tool = RDK.Item('R6Tool')

    R5 = RDK.Item('R5')
    R6 = RDK.Item('R6')

    R5Base = RDK.Item('R5Base')
    R6Base = RDK.Item('R6Base')

    HoodBrownBase = RDK.Item('HoodBrownBase')
    HoodRedBase = RDK.Item('HoodRedBase')
    HoodBlueBase = RDK.Item('HoodBlueBase')

    FrontWindowBase= RDK.Item('FrontWindowBase')
    BackWindowBase = RDK.Item('BackWindowBase')

    #R5 Points
    R5Place = RDK.Item('R5Place')
    R5PrePlace = RDK.Item('R5PrePlace')
    R5Home = RDK.Item('R5Home')
    R5Int1 = RDK.Item('R5Int1')
    R5Int2 = RDK.Item('R5Int2')
    R5Int3 = RDK.Item('R5Int3')
    R5Int4 = RDK.Item('R5Int4')
    R5Int5 = RDK.Item('R5Int5')
    R5BluePick = RDK.Item('R5BluePick')
    R5BluePrePick = RDK.Item('R5BluePrePick')
    R5RedPick = RDK.Item('R5RedPick')
    R5RedPrePick = RDK.Item('R5RedPrePick')
    R5BrownPick = RDK.Item('R5BrownPick')
    R5BrownPrePick = RDK.Item('R5BrownPrePick')

    #R6 Points
    R6FrontPlace = RDK.Item('R6FrontPlace')
    R6FrontPrePlace = RDK.Item('R6FrontPrePlace')
    R6BackPlace = RDK.Item('R6BackPlace')
    R6BackPrePlace = RDK.Item('R6BackPrePlace')
    R6FrontPick = RDK.Item('R6FrontPick')
    R6FrontPrePick = RDK.Item('R6FrontPrePick')
    R6BackPick = RDK.Item('R6BackPick')
    R6BackPrePick = RDK.Item('R6BackPrePick')
    R6Home = RDK.Item('R6Home')
    R6Int1 = RDK.Item('R6Int1')
    R6Int2 = RDK.Item('R6Int2')
    R6Int3 = RDK.Item('R6Int3')
    R6Int4 = RDK.Item('R6Int4')

    #Move Home
    R5.setPoseFrame(R5Base)
    R6.setPoseFrame(R6Base)

    

    if color == "Red":
        R5.MoveJ(R5Home, blocking=False)
        R6.MoveJ(R6Home, blocking=False)

        R6.MoveJ(R6Int4, blocking=False)
        R5.MoveJ(R5Int2, blocking=False)
        R5.MoveJ(R5Int4, blocking=False)

        R6.MoveJ(R6BackPrePick, blocking=False)
        R5.MoveJ(R5RedPrePick, blocking=False)

        R6.MoveL(R6BackPick, blocking=False)
        R5.MoveL(R5RedPick, blocking=False)

        while R5.Busy() or R6.Busy():
            a = 1

        #TODO:Attach
        pose_abs = HoodRedBase.PoseAbs()
        HoodRedBase.setParent(R5Tool)
        HoodRedBase.setPoseAbs(pose_abs)

        pose_abs = BackWindowBase.PoseAbs()
        BackWindowBase.setParent(R6Tool)
        BackWindowBase.setPoseAbs(pose_abs)

        R6.MoveL(R6BackPrePick, blocking=False)
        R5.MoveL(R5RedPrePick, blocking=False)

        R6.MoveJ(R6Int4, blocking=False)
        R5.MoveJ(R5Int4, blocking=False)

        R5.MoveJ(R5Int2, blocking=False)
        R6.MoveJ(R6BackPlace, blocking=False)

        R5.MoveJ(R5PrePlace, blocking=False)
        R6.MoveL(R6BackPlace, blocking=False)

        R5.MoveJ(R5Place, blocking=False)

        while R5.Busy() or R6.Busy():
            a = 1

        pose_abs = HoodRedBase.PoseAbs()
        HoodRedBase.setParent(CarBase)
        HoodRedBase.setPoseAbs(pose_abs)

        pose_abs = BackWindowBase.PoseAbs()
        BackWindowBase.setParent(CarBase)
        BackWindowBase.setPoseAbs(pose_abs)

        R5.MoveJ(R5PrePlace, blocking=False)
        R6.MoveL(R6BackPrePlace, blocking=False)

        R5.MoveJ(R5Home, blocking=False)



    
    if color == "Blue":
        R5.MoveJ(R5Home, blocking=False)
        R6.MoveJ(R6Home, blocking=False)
        R5.MoveJ(R5Int2, blocking=False)
        R6.MoveJ(R6Int4, blocking=False)
        R5.MoveJ(R5Int5, blocking=False)
        R6.MoveJ(R6BackPrePick, blocking=False)
        R5.MoveJ(R5BluePrePick, blocking=False)
        R6.MoveL(R6BackPick, blocking=False)
        R5.MoveL(R5BluePick, blocking=False)

        #TODO:Attach
        pose_abs = HoodBlueBase.PoseAbs()
        HoodBlueBase.setParent(R5Tool)
        HoodBlueBase.setPoseAbs(pose_abs)

        pose_abs = BackWindowBase.PoseAbs()
        BackWindowBase.setParent(R6Tool)
        BackWindowBase.setPoseAbs(pose_abs)


    if color == "Brown":
        R5.MoveJ(R5Home, blocking=False)
        R6.MoveJ(R6Home, blocking=False)

        R6.MoveL(R6Int4, blocking=False)
        R5.MoveJ(R5Int3, blocking=False)

        R6.MoveJ(R6BackPrePick, blocking=False)
        R5.MoveL(R5BrownPrePick, blocking=False)

        R6.MoveL(R6BackPick, blocking=False)
        R5.MoveL(R5BrownPick, blocking=False)

        #TODO:Attach
        pose_abs = HoodBrownBase.PoseAbs()
        HoodBrownBase.setParent(R5Tool)
        HoodBrownBase.setPoseAbs(pose_abs)

        pose_abs = BackWindowBase.PoseAbs()
        BackWindowBase.setParent(R6Tool)
        BackWindowBase.setPoseAbs(pose_abs)
    
    while R5.Busy() or R6.Busy():
        a = 1

     
if __name__ == "__main__":
    station2("Red")
