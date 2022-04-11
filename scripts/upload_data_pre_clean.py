from pydoc import describe
import pymongo
from pymongo import MongoClient

cluster = MongoClient("mongodb+srv://research:research@kagglenotebookanalysis.lbykx.mongodb.net/test")
db = cluster["NotebookAlternatives"]
# collection = db["DataPreprocessing"]
collection = db["DataCleaning"]

# fp = "../spreadsheets/alternatives/new_cv/data_preprocessing_new.csv"
fp = "../spreadsheets/alternatives/new_cv/data_cleaning_new.csv"

isID = True
with open(fp, 'r', encoding='utf8') as f:
    IDs = []
    lines = []
    description = ""
    for line in f:
        words = line.split(",")
        if isID:
            description = words[0]
            IDs = []
        else:
            lines = []
        for i in range(len(words)-1):
            if words[i+1] == '' or words[i+1] == '\n' or words[i+1] == ' ':
                continue
            if isID:
                IDs.append(words[i+1].replace("\n",""))
            else:
                lines.append(words[i+1].replace("\n",""))
        if len(lines) == len(IDs):
            for i in range(len(lines)):
                data = {}
                data["description"] = description
                data["Notebook ID"] = IDs[i]
                data["Version ID"] = "latest"
                data["Line Number"] = lines[i]
                print(data)
                collection.insert_one(data)
        isID = not isID