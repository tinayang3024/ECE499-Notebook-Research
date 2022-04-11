import pymongo
from pymongo import MongoClient

cluster = MongoClient("mongodb+srv://research:research@kagglenotebookanalysis.lbykx.mongodb.net/test")
db = cluster["NotebookAlternatives"]
collection = db["Hyperparameter"]
# collection = db["ModelArchitecture"]

fp = "../spreadsheets/alternatives/new_nlp/hyperparameter_new.csv"
# fp = "../spreadsheets/alternatives/new_nlp/model_arc_new.csv"

with open(fp, 'r', encoding='utf8') as f:
    for line in f:
        words = line.split(",")
        for i in range(len(words)-1):
            if words[i+1] == '' or words[i+1] == '\n' or words[i+1] == ' ':
                continue
            data = {}
            data["description"] = words[0].strip()
            data["Notebook ID"] = words[i+1].replace('\n','')
            print(data)
            collection.insert_one(data)
