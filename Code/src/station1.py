from robodk import robolink
import robodk

def station1(color):
    RDK = robolink.Robolink()

    CarBase = RDK.Item("Car_Base")

    R1Tool = RDK.Item('R1Tool')
    R2Tool = RDK.Item('R2Tool')
    R3Tool = RDK.Item('R3Tool')
    R4Tool = RDK.Item('R4Tool')

    R1 = RDK.Item('R1')
    R2 = RDK.Item('R2')
    R3 = RDK.Item('R3')
    R4 = RDK.Item('R4')

    R1Base = RDK.Item('R1Base')
    R2Base = RDK.Item('R2Base')
    R3Base = RDK.Item('R3Base')
    R4Base = RDK.Item('R4Base')

    R1BlueBase = RDK.Item('R1BlueBase')
    R1BrownBase = RDK.Item('R1BrownBase')
    R1RedBase = RDK.Item('R1RedBase')
    
    R2BlueBase = RDK.Item('R2BlueBase')
    R2BrownBase = RDK.Item('R2BrownBase')
    R2RedBase = RDK.Item('R2RedBase')

    R3BlueBase = RDK.Item('R3BlueBase')
    R3BrownBase = RDK.Item('R3BrownBase')
    R3RedBase = RDK.Item('R3RedBase')
    
    R4BlueBase = RDK.Item('R4BlueBase')
    R4BrownBase = RDK.Item('R4BrownBase')
    R4RedBase = RDK.Item('R4RedBase')

    #R1 Points
    R1Place = RDK.Item('R1Place')
    R1PrePlace = RDK.Item('R1PrePlace')
    R1Home = RDK.Item('R1Home')
    R1Int1 = RDK.Item('R1Int1')
    R1Int2 = RDK.Item('R1Int2')
    R1BluePick = RDK.Item('R1BluePick')
    R1BluePrePick = RDK.Item('R1BluePrePick')
    R1RedPick = RDK.Item('R1RedPick')
    R1RedPrePick = RDK.Item('R1RedPrePick')
    R1BrownPick = RDK.Item('R1BrownPick')
    R1BrownPrePick = RDK.Item('R1BrownPrePick')

    #R2 Points
    R2Place = RDK.Item('R2Place')
    R2PrePlace = RDK.Item('R2PrePlace')
    R2Home = RDK.Item('R2Home')
    R2Int1 = RDK.Item('R2Int1')
    R2Int2 = RDK.Item('R2Int2')
    R2BluePick = RDK.Item('R2BluePick')
    R2BluePrePick = RDK.Item('R2BluePrePick')
    R2RedPick = RDK.Item('R2RedPick')
    R2RedPrePick = RDK.Item('R2RedPrePick')
    R2BrownPick = RDK.Item('R2BrownPick')
    R2BrownPrePick = RDK.Item('R2BrownPrePick')

    #R3 Points
    R3Place = RDK.Item('R3Place')
    R3PrePlace = RDK.Item('R3PrePlace')
    R3Home = RDK.Item('R3Home')
    R3Int1 = RDK.Item('R3Int1')
    R3Int2 = RDK.Item('R3Int2')
    R3BluePick = RDK.Item('R3BluePick')
    R3BluePrePick = RDK.Item('R3BluePrePick')
    R3RedPick = RDK.Item('R3RedPick')
    R3RedPrePick = RDK.Item('R3RedPrePick')
    R3BrownPick = RDK.Item('R3BrownPick')
    R3BrownPrePick = RDK.Item('R3BrownPrePick')

    #R4 Points
    R4Place = RDK.Item('R4Place')
    R4PrePlace = RDK.Item('R4PrePlace')
    R4Home = RDK.Item('R4Home')
    R4Int1 = RDK.Item('R4Int1')
    R4Int2 = RDK.Item('R4Int2')
    R4BluePick = RDK.Item('R4BluePick')
    R4BluePrePick = RDK.Item('R4BluePrePick')
    R4RedPick = RDK.Item('R4RedPick')
    R4RedPrePick = RDK.Item('R4RedPrePick')
    R4BrownPick = RDK.Item('R4BrownPick')
    R4BrownPrePick = RDK.Item('R4BrownPrePick')

    RBBlue = RDK.Item("Dreapta_Spate_Albastru")
    RBRed = RDK.Item("Dreapta_Spate")
    RBBrown = RDK.Item("Dreapta_Spate_Maro")

    RFBlue = RDK.Item("Dreapta_Fata_Albastru")
    RFRed = RDK.Item("Dreapta_Fata")
    RFBrown = RDK.Item("Dreapta_Fata_Maro")

    LBBlue = RDK.Item("Stanga_Spate_Albastru")
    LBRed = RDK.Item("Stanga_Spate")
    LBBrown = RDK.Item("Stanga_Spate_Maro")

    LFBlue = RDK.Item("Stanga_Spate_Albastru")
    LFRed = RDK.Item("Stanga_Spate")
    LFBrown = RDK.Item("Stanga_Spate_Maro")


    #Move Home
    R1.setPoseFrame(R1Base)
    R2.setPoseFrame(R2Base)
    R3.setPoseFrame(R3Base)
    R4.setPoseFrame(R4Base)


    R1.MoveJ(R1Home, blocking=False)
    R2.MoveJ(R2Home, blocking=False)
    R3.MoveJ(R3Home, blocking=False)
    R4.MoveJ(R4Home, blocking=False)

    if color == "Red":
        R1.MoveJ(R1Int1, blocking=False)
        R2.MoveJ(R2Int1, blocking=False)
        R3.MoveJ(R3Int1, blocking=False)
        R4.MoveJ(R4Int1, blocking=False)

        R1.MoveJ(R1Int2, blocking=False)

        R1.MoveJ(R1RedPrePick, blocking=False)
        R2.MoveJ(R2RedPrePick, blocking=False)
        R3.MoveJ(R3RedPrePick, blocking=False)
        R4.MoveJ(R4RedPrePick, blocking=False)

        #Pick
        R1.MoveL(R1RedPick, blocking=False)
        R2.MoveL(R2RedPick, blocking=False)
        R3.MoveL(R3RedPick, blocking=False)
        R4.MoveL(R4RedPick, blocking=False)

        while R1.Busy() or R2.Busy() or R3.Busy() or R4.Busy():
            a = 1

         #TODO:Attach
        pose_abs = R1RedBase.PoseAbs()
        R1RedBase.setParent(R1Tool)
        R1RedBase.setPoseAbs(pose_abs)

        pose_abs = R2RedBase.PoseAbs()
        R2RedBase.setParent(R2Tool)
        R2RedBase.setPoseAbs(pose_abs)

        pose_abs = R3RedBase.PoseAbs()
        R3RedBase.setParent(R3Tool)
        R3RedBase.setPoseAbs(pose_abs)

        pose_abs = R4RedBase.PoseAbs()
        R4RedBase.setParent(R4Tool)
        R4RedBase.setPoseAbs(pose_abs)

        #Prepick
        R1.MoveL(R1RedPrePick, blocking=False)
        R2.MoveL(R2RedPrePick, blocking=False)
        R3.MoveL(R3RedPrePick, blocking=False)
        R4.MoveL(R4RedPrePick, blocking=False)

        R2.MoveJ(R2Int2, blocking=False)

        R1.MoveJ(R1Int1, blocking=False)
        R2.MoveJ(R2Int1, blocking=False)
        R3.MoveJ(R3Int1, blocking=False)
        R4.MoveJ(R4Int1, blocking=False)

        R1.MoveJ(R1Home, blocking=False)
        R2.MoveJ(R2Home, blocking=False)
        R3.MoveJ(R3Home, blocking=False)
        R4.MoveJ(R4Home, blocking=False)

        R1.MoveJ(R1PrePlace, blocking=False)
        R2.MoveJ(R2PrePlace, blocking=False)
        R3.MoveJ(R3PrePlace, blocking=False)
        R4.MoveJ(R4PrePlace, blocking=False)

        R1.MoveL(R1Place, blocking=False)
        R2.MoveL(R2Place, blocking=False)
        R3.MoveL(R3Place, blocking=False)
        R4.MoveL(R4Place, blocking=False)

        #TODO: DETACH
        while R1.Busy() or R2.Busy() or R3.Busy() or R4.Busy():
            a = 1
            
        pose_abs = R1RedBase.PoseAbs()
        R1RedBase.setParent(CarBase)
        R1RedBase.setPoseAbs(pose_abs)

        pose_abs = R2RedBase.PoseAbs()
        R2RedBase.setParent(CarBase)
        R2RedBase.setPoseAbs(pose_abs)

        pose_abs = R3RedBase.PoseAbs()
        R3RedBase.setParent(CarBase)
        R3RedBase.setPoseAbs(pose_abs)

        pose_abs = R4RedBase.PoseAbs()
        R4RedBase.setParent(CarBase)
        R4RedBase.setPoseAbs(pose_abs)

        R1.MoveL(R1PrePlace, blocking=False)
        R2.MoveL(R2PrePlace, blocking=False)
        R3.MoveL(R3PrePlace, blocking=False)
        R4.MoveL(R4PrePlace, blocking=False)

        R1.MoveJ(R1Home, blocking=False)
        R2.MoveJ(R2Home, blocking=False)
        R3.MoveJ(R3Home, blocking=False)
        R4.MoveJ(R4Home, blocking=False)

    
    if color == "Blue":
        R1.MoveJ(R1Int1, blocking=False)
        R2.MoveJ(R2Int1, blocking=False)
        R4.MoveJ(R4Int1, blocking=False)

        R4.MoveJ(R4Int2, blocking=False)

        R1.MoveL(R1BluePrePick, blocking=False)
        R2.MoveL(R2BluePrePick, blocking=False)
        R3.MoveL(R3BluePrePick, blocking=False)
        R4.MoveL(R4BluePrePick, blocking=False)

        R1.MoveL(R1BluePick, blocking=False)
        R2.MoveL(R2BluePick, blocking=False)
        R3.MoveL(R3BluePick, blocking=False)
        R4.MoveL(R4BluePick, blocking=False)

        while R1.Busy() or R2.Busy() or R3.Busy() or R4.Busy():
            a = 1

         #TODO:Attach
        pose_abs = R1BlueBase.PoseAbs()
        R1BlueBase.setParent(R1Tool)
        R1BlueBase.setPoseAbs(pose_abs)

        pose_abs = R2BlueBase.PoseAbs()
        R2BlueBase.setParent(R2Tool)
        R2BlueBase.setPoseAbs(pose_abs)

        pose_abs = R3BlueBase.PoseAbs()
        R3BlueBase.setParent(R3Tool)
        R3BlueBase.setPoseAbs(pose_abs)

        pose_abs = R4BlueBase.PoseAbs()
        R4BlueBase.setParent(R4Tool)
        R4BlueBase.setPoseAbs(pose_abs)

        R1.MoveL(R1BluePrePick, blocking=False)
        R2.MoveL(R2BluePrePick, blocking=False)
        R3.MoveL(R3BluePrePick, blocking=False)
        R4.MoveL(R4BluePrePick, blocking=False)

        R4.MoveJ(R4Int1, blocking=False)

        R1.MoveJ(R1Home, blocking=False)
        R2.MoveJ(R2Home, blocking=False)
        R3.MoveJ(R3Home, blocking=False)
        R4.MoveJ(R4Home, blocking=False)

        R1.MoveJ(R1PrePlace, blocking=False)
        R2.MoveJ(R2PrePlace, blocking=False)
        R3.MoveJ(R3PrePlace, blocking=False)
        R4.MoveJ(R4PrePlace, blocking=False)

        R1.MoveL(R1Place, blocking=False)
        R2.MoveL(R2Place, blocking=False)
        R3.MoveL(R3Place, blocking=False)
        R4.MoveL(R4Place, blocking=False)

        #TODO: DETACH
        while R1.Busy() or R2.Busy() or R3.Busy() or R4.Busy():
            a = 1
            
        pose_abs = R1BlueBase.PoseAbs()
        R1BlueBase.setParent(CarBase)
        R1BlueBase.setPoseAbs(pose_abs)

        pose_abs = R2BlueBase.PoseAbs()
        R2BlueBase.setParent(CarBase)
        R2BlueBase.setPoseAbs(pose_abs)

        pose_abs = R3BlueBase.PoseAbs()
        R3BlueBase.setParent(CarBase)
        R3BlueBase.setPoseAbs(pose_abs)

        pose_abs = R4BlueBase.PoseAbs()
        R4BlueBase.setParent(CarBase)
        R4BlueBase.setPoseAbs(pose_abs)

        R1.MoveL(R1PrePlace, blocking=False)
        R2.MoveL(R2PrePlace, blocking=False)
        R3.MoveL(R3PrePlace, blocking=False)
        R4.MoveL(R4PrePlace, blocking=False)

        R1.MoveJ(R1Home, blocking=False)
        R2.MoveJ(R2Home, blocking=False)
        R3.MoveJ(R3Home, blocking=False)
        R4.MoveJ(R4Home, blocking=False)


    if color == "Brown":
        R1.MoveJ(R1Int1, blocking=False)
        R2.MoveJ(R2Int1, blocking=False)
        R4.MoveJ(R4Int1, blocking=False)

        R4.MoveJ(R4Int2, blocking=False)

        R1.MoveL(R1BrownPrePick, blocking=False)
        R2.MoveL(R2BrownPrePick, blocking=False)
        R3.MoveL(R3BrownPrePick, blocking=False)
        R4.MoveL(R4BrownPrePick, blocking=False)

        R1.MoveL(R1BrownPick, blocking=False)
        R2.MoveL(R2BrownPick, blocking=False)
        R3.MoveL(R3BrownPick, blocking=False)
        R4.MoveL(R4BrownPick, blocking=False)

        while R1.Busy() or R2.Busy() or R3.Busy() or R4.Busy():
            a = 1

         #TODO:Attach
        pose_abs = R1BrownBase.PoseAbs()
        R1BrownBase.setParent(R1Tool)
        R1BrownBase.setPoseAbs(pose_abs)

        pose_abs = R2BrownBase.PoseAbs()
        R2BrownBase.setParent(R2Tool)
        R2BrownBase.setPoseAbs(pose_abs)

        pose_abs = R3BrownBase.PoseAbs()
        R3BrownBase.setParent(R3Tool)
        R3BrownBase.setPoseAbs(pose_abs)

        pose_abs = R4BrownBase.PoseAbs()
        R4BrownBase.setParent(R4Tool)
        R4BrownBase.setPoseAbs(pose_abs)

        R1.MoveL(R1BrownPrePick, blocking=False)
        R2.MoveL(R2BrownPrePick, blocking=False)
        R3.MoveL(R3BrownPrePick, blocking=False)
        R4.MoveL(R4BrownPrePick, blocking=False)

        R4.MoveJ(R4Int1, blocking=False)

        R1.MoveJ(R1Home, blocking=False)
        R2.MoveJ(R2Home, blocking=False)
        R3.MoveJ(R3Home, blocking=False)
        R4.MoveJ(R4Home, blocking=False)

        R1.MoveJ(R1PrePlace, blocking=False)
        R2.MoveJ(R2PrePlace, blocking=False)
        R3.MoveJ(R3PrePlace, blocking=False)
        R4.MoveJ(R4PrePlace, blocking=False)

        R1.MoveL(R1Place, blocking=False)
        R2.MoveL(R2Place, blocking=False)
        R3.MoveL(R3Place, blocking=False)
        R4.MoveL(R4Place, blocking=False)

        #TODO: DETACH
         #TODO:Attach

        while R1.Busy() or R2.Busy() or R3.Busy() or R4.Busy():
            a = 1

        pose_abs = R1BrownBase.PoseAbs()
        R1BrownBase.setParent(CarBase)
        R1BrownBase.setPoseAbs(pose_abs)

        pose_abs = R2BrownBase.PoseAbs()
        R2BrownBase.setParent(CarBase)
        R2BrownBase.setPoseAbs(pose_abs)

        pose_abs = R3BrownBase.PoseAbs()
        R3BrownBase.setParent(CarBase)
        R3BrownBase.setPoseAbs(pose_abs)

        pose_abs = R4BrownBase.PoseAbs()
        R4BrownBase.setParent(CarBase)
        R4BrownBase.setPoseAbs(pose_abs)


        R1.MoveL(R1PrePlace, blocking=False)
        R2.MoveL(R2PrePlace, blocking=False)
        R3.MoveL(R3PrePlace, blocking=False)
        R4.MoveL(R4PrePlace, blocking=False)

        R1.MoveJ(R1Home, blocking=False)
        R2.MoveJ(R2Home, blocking=False)
        R3.MoveJ(R3Home, blocking=False)
        R4.MoveJ(R4Home, blocking=False)
    
        
if __name__ == "__main__":
    station1("Blue")
