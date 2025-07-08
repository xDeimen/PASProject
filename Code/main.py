from src.station1 import station1
from src.station2 import station2
from inventory_service import *
from src.line import copy_line
from utils.color import get_random_color
from src.run import run

uri = "mongodb://localhost:27017/"

inventory = InventoryService(uri, "prod_db", "inventory")

i = 1

while i <= 1:
    color = get_random_color()
    attach_to = copy_line(i, color)
    inventory.copy_necesarry(i, color)
    run(attach_to, color, i)
    inventory.finish(increment=i, color=color)
    i = i + 1 