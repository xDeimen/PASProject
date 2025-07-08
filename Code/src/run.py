from src.station1 import station1
from src.station2 import station2
from robodk import robolink

def run(obj_to_attach_to, color, increment):
    RDK = robolink.Robolink()
    line = RDK.Item(f"Line_{increment}")
    home = RDK.Item(f"Home_{increment}")
    s1 = RDK.Item(f"Station1_{increment}")
    s2 = RDK.Item(f"Station2_{increment}")
    s3 = RDK.Item(f"Station3_{increment}")
    s4 = RDK.Item(f"Station4_{increment}")
    s5 = RDK.Item(f"Station5_{increment}")

    line.MoveL(home)
    while line.Busy():
        a=1 

    line.MoveL(s1)
    while line.Busy():
        a=1 

    station1(obj_to_attach_to, color, increment)
    
    line.MoveL(s2)
    while line.Busy():
        a=1
    
    station2(obj_to_attach_to, color, increment)

    line.MoveL(s3)
    while line.Busy():
        a=1

    