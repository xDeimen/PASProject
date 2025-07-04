from robot import Robot

class Station:
    def __init__(self,robots:Robot):
        self.robots = robots

    def run_station(self):
        for robot in self.robots:
            robot.run_sequences()