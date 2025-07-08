from utils.mongo import MongoDBInterface
from bson.objectid import ObjectId
from robodk import robolink

class StatsClass:
    def __init__(self):
        self.interface = MongoDBInterface(
            "mongodb://localhost:27017/",
            "prod_db",
            "logs",)
        
    def log(self, 
        product_increment,
        station,
        robots,
        move,
        target,
        start_time ,
        end_time
    ):
        for index in range(len(robots)):
            log = {
                "product_increment": product_increment,
                "station": station,
                "robot": robots[index],
                "move": move,
                "targets": target[index],
                "start_time": start_time,
                "end_time": end_time,


            }
            self.interface.create_document(log)
        