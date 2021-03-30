import json

class Increments:
    def upjson(bouton_ID):
        file = open("buttons.json","r")
        object_json = json.load(file)
        object_json[bouton_ID]["clicks"] = object_json[bouton_ID]["clicks"] + 1
        file = open("buttons.json","w")
        json.dump(object_json,file)
        file.close()