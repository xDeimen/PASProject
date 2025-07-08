from robodk import robolink

def get_all_children(item):
    children = []
    for child in item.Childs():
        children.append(child)
        children.extend(get_all_children(child))
    return children


def copy_line(increment, color):
    RDK = robolink.Robolink()
    original_frame = RDK.Item('LineBase', robolink.ITEM_TYPE_FRAME)
    print(original_frame)

    copied_frame = original_frame.Copy()
    copied_frame = RDK.Paste()

    copied_frame.setName(f'LineBase_{increment}')

    children = get_all_children(copied_frame)

    for item in children:
        old_name = item.Name()
        new_name = f"{old_name}_{increment}"
        item.setName(new_name)

    car = RDK.Item(f"Baza_{color}_{increment}")
    car.setVisible(True)

    support = RDK.Item(f"Support_{increment}")
    support.setVisible(True)

    targets = [
        RDK.Item(f"Station1_{increment}"),
        RDK.Item(f"Home_{increment}"),
        RDK.Item(f"Station2_{increment}"),
        RDK.Item(f"Station3_{increment}"),
        RDK.Item(f"Station4_{increment}"),
        RDK.Item(f"Station5_{increment}"),
        RDK.Item(f"END_{increment}")
    ]
    for target in targets:
        target.setRobot(RDK.Item(f"Line_{increment}"))

    object_to_attach_to = RDK.Item(f"Line_{increment}")

    return object_to_attach_to

if __name__ == "__main__":
    copy_line(3, "Red")