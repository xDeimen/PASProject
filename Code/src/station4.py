from src.station3 import station3
from robodk import robolink

def station4(obj, increment, iteration=1):
    RDK = robolink.Robolink()

    R8 = RDK.Item('R8')
    R10 = RDK.Item('R10')

    R8Base = RDK.Item('R8Base')
    R10Base = RDK.Item('R10Base')


    #R7 Points
    R8Home = RDK.Item('R8Home')
    R8Int = RDK.Item('R8Int')
    R8_1 = RDK.Item('R9_1')
    R8_2 = RDK.Item('R9_2')
    R8_3 = RDK.Item('R9_3')
    R8_4 = RDK.Item('R9_4')
    R8_5 = RDK.Item('R9_5')
    R8_6 = RDK.Item('R9_6')
    R8_7 = RDK.Item('R9_7')
    R8_8 = RDK.Item('R9_8')
    R8_9 = RDK.Item('R9_9')
    R8_10 = RDK.Item('R9_10')

    #R10 Points
    R10Home = RDK.Item('R10Home')
    R10Int = RDK.Item('R10Int')
    R10_1 = RDK.Item('R10_1')
    R10_2 = RDK.Item('R10_2')
    R10_3 = RDK.Item('R10_3')
    R10_4 = RDK.Item('R10_4')
    R10_5 = RDK.Item('R10_5')
    R10_6 = RDK.Item('R10_6')
    R10_7 = RDK.Item('R10_7')
    R10_8 = RDK.Item('R10_8')
    R10_9 = RDK.Item('R10_9')
    R10_10 = RDK.Item('R10_10')
   
    #Move Home
    R8.setPoseFrame(R8Base)
    R10.setPoseFrame(R10Base)
    if iteration==2:
        station3(obj, increment, 2)

    R8.MoveJ(R8Int, blocking=False)
    R10.MoveJ(R10Int, blocking=False)

    R8.MoveL(R8_1, blocking=False)
    R10.MoveL(R10_1, blocking=False)

    R8.MoveL(R8_2, blocking=False)
    R10.MoveL(R10_2, blocking=False)

    R8.MoveL(R8_1, blocking=False)
    R10.MoveL(R10_1, blocking=False)

    R8.MoveL(R8_3, blocking=False)
    R10.MoveL(R10_3, blocking=False)

    R8.MoveL(R8_4, blocking=False)
    R10.MoveL(R10_4, blocking=False)

    R8.MoveL(R8_3, blocking=False)
    R10.MoveL(R10_3, blocking=False)

    R8.MoveL(R8_5, blocking=False)
    R10.MoveL(R10_5, blocking=False)

    R8.MoveL(R8_6, blocking=False)
    R10.MoveL(R10_6, blocking=False)

    R8.MoveL(R8_5, blocking=False)
    R10.MoveL(R10_5, blocking=False)

    R8.MoveL(R8_7, blocking=False)
    R10.MoveL(R10_7, blocking=False)

    R8.MoveL(R8_8, blocking=False)
    R10.MoveL(R10_8, blocking=False)

    R8.MoveL(R8_7, blocking=False)
    R10.MoveL(R10_7, blocking=False)

    R8.MoveL(R8_9, blocking=False)
    R10.MoveL(R10_9, blocking=False)

    R8.MoveL(R8_10, blocking=False)
    R10.MoveL(R10_10, blocking=False)

    R8.MoveL(R8_9, blocking=False)
    R10.MoveL(R10_9, blocking=False)

    R8.MoveJ(R8Home, blocking=False)
    R10.MoveL(R10Home, blocking=False)