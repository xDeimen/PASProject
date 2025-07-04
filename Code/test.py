from robodk import robolink
import threading
import time

# Initialize RoboDK connection
RDK = robolink.Robolink()

def move_robot_to_targets(robot, target_names, robot_name, base):
    """
    Move a single robot through a sequence of pre-configured targets
    
    Args:
        robot: Robot object from RoboDK
        target_names: List of target names (strings) as they appear in RoboDK
        robot_name: Name of the robot for logging
    """
    print(f"Starting movement sequence for {robot_name}")
    
    for i, target_name in enumerate(target_names):
        try:
            # Get the target from RoboDK station
            target = RDK.Item(target_name, robolink.ITEM_TYPE_TARGET)
            
            if not target.Valid():
                print(f"Error: Target '{target_name}' not found for {robot_name}")
                continue
            
            robot.setFrame(base)
            robot.MoveJ(target, )
            print(f"{robot_name}: Reached target '{target_name}' ({i+1}/{len(target_names)})")
            
        except Exception as e:
            print(f"Error moving {robot_name} to target '{target_name}': {e}")
            break
    
    print(f"Completed movement sequence for {robot_name}")

def main():
    r1_frame = RDK.Item("R1Base")
    r2_frame = RDK.Item("R2Base")
    robot1_name = "R1"
    robot2_name = "R2"
    
    robot1 = RDK.Item(robot1_name, robolink.ITEM_TYPE_ROBOT)
    
    robot2 = RDK.Item(robot2_name, robolink.ITEM_TYPE_ROBOT)
    
    # Check if robots exist
    if not robot1.Valid():
        print(f"Error: Robot '{robot1_name}' not found")
        return
    if not robot2.Valid():
        print(f"Error: Robot '{robot2_name}' not found")
        return
    
    print(f"Robot 1: {robot1.Name()}")
    print(f"Robot 2: {robot2.Name()}")
    
    robot1_targets = [
        "R1Int",
        "R1Home",    # First target for Robot 1
        "R1PrePlace",    # Second target for Robot 1
        "R1Place"
    ]
    
    robot2_targets = [
        "R2Int",
        "R2Home",    # First target for Robot 2
        "R2PrePlace",    # Second target for Robot 2
        "R2Place",    # Third target for Robot 2
              # Home position for Robot 2
    ]
    
    # Optional: Set movement parameters
    robot1.setSpeed(100)  # mm/s
    robot2.setSpeed(100)
    
    # Create threads for simultaneous movement
    thread1 = threading.Thread(
        target=move_robot_to_targets, 
        args=(robot1, robot1_targets, robot1.Name(), r1_frame)
    )
    
    thread2 = threading.Thread(
        target=move_robot_to_targets, 
        args=(robot2, robot2_targets, robot2.Name(), r2_frame)
    )
    
    print("Starting simultaneous robot movements...")
    print("-" * 50)
    
    # Start both threads simultaneously
    thread1.start()
    thread2.start()
    
    # Wait for both threads to complete
    thread1.join()
    thread2.join()
    
    print("-" * 50)
    print("All robots have completed their movements!")


if __name__ == "__main__":
    try:

        main()
        
        
    except Exception as e:
        print(f"Script error: {e}")
    
    print("Script completed!")