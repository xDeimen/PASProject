from utils.mongo import MongoDBInterface
from bson.objectid import ObjectId
from robodk import robolink


COLOR_MAP = {
    "Red":"Rosie",
    "Blue":"Albastra",
    "Brown":"Maro"
}

class InventoryService:
    def __init__(self, uri, db, table):
        self.interface = MongoDBInterface(uri, db, table)
        self.logs = MongoDBInterface(uri, db, "logs")
        self.products = MongoDBInterface(uri, db, "products")
        self.inventory = self.interface.read_documents()[0]


    def _update(self):
        query = {"_id": ObjectId('686d3179383e4ddc77325f3d')}
        self.interface.update_document(query, self.inventory)


    def consume_doors(self, color):
        color = COLOR_MAP[color]
        """
        Rosie
        Albastra
        Maro
        """
        self.inventory[f"Usa_Stanga_Spate_{color}"] = self.inventory[f"Usa_Stanga_Spate_{color}"] -1
        self.inventory[f"Usa_Stanga_Fata_{color}"] = self.inventory[f"Usa_Stanga_Fata_{color}"] -1
        self.inventory[f"Usa_Dreapta_Spate_{color}"] = self.inventory[f"Usa_Dreapta_Spate_{color}"] -1
        self.inventory[f"Usa_Dreapta_Fata_{color}"] = self.inventory[f"Usa_Dreapta_Fata_{color}"] -1

        self._update()

    def consume_wheels(self, cate_roti):
        self.inventory["Roata"] = self.inventory["Roata"] - cate_roti
        
        self._update()

    def consume_capota(self, color):
        color = COLOR_MAP[color]
        """
        Rosie
        Albastra
        Maro
        """
        self.inventory[f"Capota_{color}"] = self.inventory[f"Capota_{color}"] -1

        self._update()

    def consume_glass(self):
        self.inventory[f"Geam_Spate"] = self.inventory[f"Geam_Spate"] -1
        self.inventory[f"Geam_Fata"] = self.inventory[f"Geam_Fata"] -1

        self._update()

    def consume_all(self, color):
        self.consume_doors(color)
        self.consume_capota(color)
        self.consume_glass()
        self.consume_wheels(4)

    def _get_all_children(self, item):
        children = []
        for child in item.Childs():
            children.append(child)
            children.extend(self._get_all_children(child))
        return children

    
    def copy_necesarry(self, increment, color):
        RDK = robolink.Robolink()

        to_copy = [
            RDK.Item(f'R1{color}Base', robolink.ITEM_TYPE_FRAME),
            RDK.Item(f'R2{color}Base', robolink.ITEM_TYPE_FRAME),
            RDK.Item(f'R3{color}Base', robolink.ITEM_TYPE_FRAME),
            RDK.Item(f'R4{color}Base', robolink.ITEM_TYPE_FRAME),
            RDK.Item(f'Hood{color}Base', robolink.ITEM_TYPE_FRAME),
            RDK.Item(f'FrontWindowBase', robolink.ITEM_TYPE_FRAME),
            RDK.Item(f'BackWindowBase', robolink.ITEM_TYPE_FRAME),
            RDK.Item(f'W1', robolink.ITEM_TYPE_FRAME),
            RDK.Item(f'W2', robolink.ITEM_TYPE_FRAME),
            RDK.Item(f'W3', robolink.ITEM_TYPE_FRAME),
            RDK.Item(f'W4', robolink.ITEM_TYPE_FRAME),
        ]

        

        for copy in to_copy:
            c = copy.Copy()
            c = RDK.Paste()
            print(copy.Name)
            c.setName(f"{copy.Name()}_{increment}")
            children = self._get_all_children(c)
    
            for item in children:
                old_name = item.Name()
                new_name = f"{old_name}_{increment}"
                item.setName(new_name)

        set_visible = [
            RDK.Item(f'Capota_{color}_{increment}'),
            RDK.Item(f'Geam_Fata_{increment}'),
            RDK.Item(f'Geam_Spate_{increment}'),
            RDK.Item(f'Dreapta_Spate_{color}_{increment}'),
            RDK.Item(f'Dreapta_Fata_{color}_{increment}'),
            RDK.Item(f'Stanga_Spate_{color}_{increment}'),
            RDK.Item(f'Stanga_Fata_{color}_{increment}'),
            RDK.Item(f'W1_Roata_{increment}'),
            RDK.Item(f'W2_Roata_{increment}'),
            RDK.Item(f'W3_Roata_{increment}'),
            RDK.Item(f'W4_Roata_{increment}'),

        ]

        for item in set_visible:
            item.setVisible(True)

        self.consume_all(color)

    def finish(self, increment):
        RDK = robolink.Robolink()
        item = RDK.Item(f"LineBase_{increment}", robolink.ITEM_TYPE_FRAME)
        item.Delete()

    def get_max_increment(self):
        return self.products.get_max_value("prod_id")
    
    def log_products(self, **kwargs):
        kwargs['prod_time'] = int(kwargs['prod_time'].total_seconds())
        self.products.create_document(kwargs)
    




