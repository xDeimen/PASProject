from robodk import robolink
from stats import StatsClass
import datetime



def station1(obj_to_attach_to, color, increment):
    s = StatsClass()

    RDK = robolink.Robolink()

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

    R1ColorBase = RDK.Item(f'R1{color}Base_{increment}')
    R2ColorBase = RDK.Item(f'R2{color}Base_{increment}')
    R3ColorBase = RDK.Item(f'R3{color}Base_{increment}')
    R4ColorBase = RDK.Item(f'R4{color}Base_{increment}')

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

    #Move Home
    R1.setPoseFrame(R1Base)
    R2.setPoseFrame(R2Base)
    R3.setPoseFrame(R3Base)
    R4.setPoseFrame(R4Base)

    

    start_time = datetime.datetime.now()
    R1.MoveJ(R1Home, blocking=False)
    R2.MoveJ(R2Home, blocking=False)
    R3.MoveJ(R3Home, blocking=False)
    R4.MoveJ(R4Home, blocking=False)
    s.log(
        product_increment = increment,
        station = "S1",
        robots = ["R1", "R2", "R3", "R4"],
        move = "J",
        target = [R1Base.Name(), R2Base.Name(), R3Base.Name(), R4Base.Name()],
        start_time = start_time,
        end_time = datetime.datetime.now(),
    )

    if color == "Red":
        start_time = datetime.datetime.now()
        R1.MoveJ(R1Int1, blocking=False)
        R2.MoveJ(R2Int1, blocking=False)
        R3.MoveJ(R3Int1, blocking=False)
        R4.MoveJ(R4Int1, blocking=False)

        s.log(
            product_increment = increment,
            station = "S1",
            robots = ["R1", "R2", "R3", "R4"],
            move = "J",
            target = [R1Int1.Name(), R2Int1.Name(), R3Int1.Name(), R4Int1.Name()],
            start_time = start_time,
            end_time = datetime.datetime.now(),
        )

        R1.MoveJ(R1Int2, blocking=False)

        R1.MoveJ(R1RedPrePick, blocking=False)
        R2.MoveJ(R2RedPrePick, blocking=False)
        R3.MoveJ(R3RedPrePick, blocking=False)
        R4.MoveJ(R4RedPrePick, blocking=False)

        start_time = datetime.datetime.now()
        s.log(
            product_increment = increment,
            station = "S1",
            robots = ["R1", "R2", "R3", "R4"],
            move = "J",
            target = [R1RedPrePick.Name(), R2RedPrePick.Name(), R3RedPrePick.Name(), R4RedPrePick.Name()],
            start_time = start_time,
            end_time = datetime.datetime.now(),
        )

        #Pick
        R1.MoveL(R1RedPick, blocking=False)
        R2.MoveL(R2RedPick, blocking=False)
        R3.MoveL(R3RedPick, blocking=False)
        R4.MoveL(R4RedPick, blocking=False)
        start_time = datetime.datetime.now()
        s.log(
            product_increment = increment,
            station = "S1",
            robots = ["R1", "R2", "R3", "R4"],
            move = "J",
            target = [R1RedPick.Name(), R2RedPick.Name(), R3RedPick.Name(), R4RedPick.Name()],
            start_time = start_time,
            end_time = datetime.datetime.now(),
        )

        while R1.Busy() or R2.Busy() or R3.Busy() or R4.Busy():
            a = 1

         #TODO:Attach
        pose_abs = R1ColorBase.PoseAbs()
        R1ColorBase.setParent(R1Tool)
        R1ColorBase.setPoseAbs(pose_abs)

        pose_abs = R2ColorBase.PoseAbs()
        R2ColorBase.setParent(R2Tool)
        R2ColorBase.setPoseAbs(pose_abs)

        pose_abs = R3ColorBase.PoseAbs()
        R3ColorBase.setParent(R3Tool)
        R3ColorBase.setPoseAbs(pose_abs)

        pose_abs = R4ColorBase.PoseAbs()
        R4ColorBase.setParent(R4Tool)
        R4ColorBase.setPoseAbs(pose_abs)

        #Prepick
        start_time = datetime.datetime.now()
        R1.MoveL(R1RedPrePick, blocking=False)
        R2.MoveL(R2RedPrePick, blocking=False)
        R3.MoveL(R3RedPrePick, blocking=False)
        R4.MoveL(R4RedPrePick, blocking=False)

        s.log(
            product_increment = increment,
            station = "S1",
            robots = ["R1", "R2", "R3", "R4"],
            move = "J",
            target = [R1RedPrePick.Name(), R2RedPrePick.Name(), R3RedPrePick.Name(), R4RedPrePick.Name()],
            start_time = start_time,
            end_time = datetime.datetime.now(),
        )

        R2.MoveJ(R2Int2, blocking=False)

        start_time = datetime.datetime.now()
        R1.MoveJ(R1Int1, blocking=False)
        R2.MoveJ(R2Int1, blocking=False)
        R3.MoveJ(R3Int1, blocking=False)
        R4.MoveJ(R4Int1, blocking=False)

        s.log(
            product_increment = increment,
            station = "S1",
            robots = ["R1", "R2", "R3", "R4"],
            move = "J",
            target = [R1Int1.Name(), R2Int1.Name(), R3Int1.Name(), R4Int1.Name()],
            start_time = start_time,
            end_time = datetime.datetime.now(),
        )



        start_time = datetime.datetime.now()
        R1.MoveJ(R1Home, blocking=False)
        R2.MoveJ(R2Home, blocking=False)
        R3.MoveJ(R3Home, blocking=False)
        R4.MoveJ(R4Home, blocking=False)

        s.log(
            product_increment = increment,
            station = "S1",
            robots = ["R1", "R2", "R3", "R4"],
            move = "J",
            target = [R1Home.Name(), R2Home.Name(), R3Home.Name(), R4Home.Name()],
            start_time = start_time,
            end_time = datetime.datetime.now(),
        )

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
            
        pose_abs = R1ColorBase.PoseAbs()
        R1ColorBase.setParent(obj_to_attach_to)
        R1ColorBase.setPoseAbs(pose_abs)

        pose_abs = R2ColorBase.PoseAbs()
        R2ColorBase.setParent(obj_to_attach_to)
        R2ColorBase.setPoseAbs(pose_abs)

        pose_abs = R3ColorBase.PoseAbs()
        R3ColorBase.setParent(obj_to_attach_to)
        R3ColorBase.setPoseAbs(pose_abs)

        pose_abs = R4ColorBase.PoseAbs()
        R4ColorBase.setParent(obj_to_attach_to)
        R4ColorBase.setPoseAbs(pose_abs)

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
        pose_abs = R1ColorBase.PoseAbs()
        R1ColorBase.setParent(R1Tool)
        R1ColorBase.setPoseAbs(pose_abs)

        pose_abs = R2ColorBase.PoseAbs()
        R2ColorBase.setParent(R2Tool)
        R2ColorBase.setPoseAbs(pose_abs)

        pose_abs = R3ColorBase.PoseAbs()
        R3ColorBase.setParent(R3Tool)
        R3ColorBase.setPoseAbs(pose_abs)

        pose_abs = R4ColorBase.PoseAbs()
        R4ColorBase.setParent(R4Tool)
        R4ColorBase.setPoseAbs(pose_abs)

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
            
        pose_abs = R1ColorBase.PoseAbs()
        R1ColorBase.setParent(obj_to_attach_to)
        R1ColorBase.setPoseAbs(pose_abs)

        pose_abs = R2ColorBase.PoseAbs()
        R2ColorBase.setParent(obj_to_attach_to)
        R2ColorBase.setPoseAbs(pose_abs)

        pose_abs = R3ColorBase.PoseAbs()
        R3ColorBase.setParent(obj_to_attach_to)
        R3ColorBase.setPoseAbs(pose_abs)

        pose_abs = R4ColorBase.PoseAbs()
        R4ColorBase.setParent(obj_to_attach_to)
        R4ColorBase.setPoseAbs(pose_abs)

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
        pose_abs = R1ColorBase.PoseAbs()
        R1ColorBase.setParent(R1Tool)
        R1ColorBase.setPoseAbs(pose_abs)

        pose_abs = R2ColorBase.PoseAbs()
        R2ColorBase.setParent(R2Tool)
        R2ColorBase.setPoseAbs(pose_abs)

        pose_abs = R3ColorBase.PoseAbs()
        R3ColorBase.setParent(R3Tool)
        R3ColorBase.setPoseAbs(pose_abs)

        pose_abs = R4ColorBase.PoseAbs()
        R4ColorBase.setParent(R4Tool)
        R4ColorBase.setPoseAbs(pose_abs)

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

        pose_abs = R1ColorBase.PoseAbs()
        R1ColorBase.setParent(obj_to_attach_to)
        R1ColorBase.setPoseAbs(pose_abs)

        pose_abs = R2ColorBase.PoseAbs()
        R2ColorBase.setParent(obj_to_attach_to)
        R2ColorBase.setPoseAbs(pose_abs)

        pose_abs = R3ColorBase.PoseAbs()
        R3ColorBase.setParent(obj_to_attach_to)
        R3ColorBase.setPoseAbs(pose_abs)

        pose_abs = R4ColorBase.PoseAbs()
        R4ColorBase.setParent(obj_to_attach_to)
        R4ColorBase.setPoseAbs(pose_abs)


        R1.MoveL(R1PrePlace, blocking=False)
        R2.MoveL(R2PrePlace, blocking=False)
        R3.MoveL(R3PrePlace, blocking=False)
        R4.MoveL(R4PrePlace, blocking=False)

        R1.MoveJ(R1Home, blocking=False)
        R2.MoveJ(R2Home, blocking=False)
        R3.MoveJ(R3Home, blocking=False)
        R4.MoveJ(R4Home, blocking=False)
    
        
if __name__ == "__main__":
    station1("Red")
