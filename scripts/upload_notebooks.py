import pymongo
from pymongo import MongoClient

cluster = MongoClient("mongodb+srv://research:research@kagglenotebookanalysis.lbykx.mongodb.net/test")
db = cluster["NotebookAlternatives"]
collection = db["NotebookInfo"]

fp = "../spreadsheets/samples/new_cv_samples.csv"

notbook_ids = ["103", "105", "109", "114", "122", "128", "137", "139", "140"]
with open(fp, 'r', encoding='utf8') as f:
    for line in f:
        words = line.split(",")
        id = words[0].strip()
        data = {}
        data["Notebook ID"] = words[-5].strip()
        if  data["Notebook ID"] in notbook_ids:
            data["General Topic"] = "CV"
            data["Notebook Link"] = words[0].strip()
            print(data)
            # collection.insert_one(data)