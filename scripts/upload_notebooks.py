import pymongo
from pymongo import MongoClient

cluster = MongoClient("mongodb+srv://research:research@kagglenotebookanalysis.lbykx.mongodb.net/test")
db = cluster["NotebookAlternatives"]
collection = db["NotebookInfo"]

fp = "../spreadsheets/samples_notebook_list/new_data_samples.csv"

notbook_ids = ["253", "258", "287", "291", "297", "351", "359"]
with open(fp, 'r', encoding='utf8') as f:
    for line in f:
        words = line.split(",")
        data = {}
        data["Notebook ID"] = words[0].strip()
        # print(data)
        if  data["Notebook ID"] in notbook_ids:
            data["General Topic"] = "Data Analytics"
            data["Notebook Link"] = words[1].strip()
            print(data)
            collection.insert_one(data)