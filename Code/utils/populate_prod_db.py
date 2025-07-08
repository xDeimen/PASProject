from mongo import MongoDBInterface

if __name__ == "__main__":
    uri = "mongodb://localhost:27017/"
    db_interface = MongoDBInterface(uri, "prod_db", "inventory")

    inventory = {
        "Usa_Stanga_Spate_Albastra" : 30,
        "Usa_Stanga_Fata_Albastra" : 30,
        "Usa_Dreapta_Spate_Albastra" : 30,
        "Usa_Dreapta_Fata_Albastra" : 30,

        "Usa_Stanga_Spate_Rosie" : 30,
        "Usa_Stanga_Fata_Rosie" : 30,
        "Usa_Dreapta_Spate_Rosie" : 30,
        "Usa_Dreapta_Fata_Rosie" : 30,

        "Usa_Stanga_Spate_Maro" : 30,
        "Usa_Stanga_Fata_Maro" : 30,
        "Usa_Dreapta_Spate_Maro" : 30,
        "Usa_Dreapta_Fata_Maro" : 30,

        "Capota_Rosie" : 30,
        "Capota_Albastra" : 30,
        "Capota_Maro" : 30,

        "Geam_Fata" : 90,
        "Geam_Spate" : 90,

        "Roata": 120

    }

    # Create
    user_id = db_interface.create_document(inventory)
    print("Inserted ID:", user_id)
