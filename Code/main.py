from src.station1 import station1
from src.station2 import station2
from inventory_service import *
from src.line import copy_line
from utils.color import get_random_color
from src.run import run
import datetime

uri = "mongodb://localhost:27017/"
inventory = InventoryService(uri, "prod_db", "inventory")

latest_product_id = inventory.get_max_increment()
instances = 5

prod_id = latest_product_id + 1

while prod_id <= latest_product_id + instances:
    #Get a random color
    color = get_random_color()

    #Get the object to attach all the parts to
    attach_to = copy_line(prod_id, color)

    #Remove from inventory the used parts
    inventory.copy_necesarry(prod_id, color)

    #Run
    start_time = datetime.datetime.now()
    run(attach_to, color, prod_id)
    end_time = datetime.datetime.now()
    inventory.finish(increment=prod_id)
    
    inventory.log_products(
        prod_id = prod_id,
        prod_time = end_time-start_time,
        color = color
        
    )

    #Next instance
    prod_id = prod_id + 1