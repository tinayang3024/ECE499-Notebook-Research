
import pymongo
from pymongo import MongoClient
import numpy as np
import matplotlib.pyplot as plt
import os

cluster = MongoClient("mongodb+srv://research:research@kagglenotebookanalysis.lbykx.mongodb.net/test", )
db = cluster["NotebookAlternatives"]
def load_notebooks():
    collection = db["NotebookInfo"]
    results = collection.find({})
    data = {}
    for res in results:
        # print(res)
        data[res["Notebook ID"]] = {}
        data[res["Notebook ID"]]["Topic"] = res["General Topic"]
        data[res["Notebook ID"]]["Link"] = res["Notebook Link"]
        data[res["Notebook ID"]]["DataCleaning"] = 0
        data[res["Notebook ID"]]["DataPreprocessing"] = 0
        data[res["Notebook ID"]]["Hyperparameter"] = 0
        data[res["Notebook ID"]]["ModelArchitecture"] = 0
    return data

def read_alt(data, key):
    collection = db[key]
    results = collection.find({})
    for res in results:
        if res["Notebook ID"] not in data:
            print ("???" + str(res["Notebook ID"]))
            continue
        data[res["Notebook ID"]][key] += 1
    return data

def filter_notebooks(data):
    new_data = {}
    for key, notebook in data.items():
        if notebook["DataCleaning"] == 0 and notebook["DataPreprocessing"] == 0 and notebook["Hyperparameter"] == 0 and notebook["ModelArchitecture"] == 0:
            print ("???~" + str(key))
            continue
        else:
            new_data[key] = notebook
    return new_data

def generate_overleaf_table(data, output_path):
    overleaf_str = ""
    for key, notebook in data.items():
        overleaf_str += key 
        overleaf_str += " & " 
        overleaf_str += str(notebook["DataCleaning"])
        overleaf_str += " & " 
        overleaf_str += str(notebook["DataPreprocessing"])
        overleaf_str += " & " 
        overleaf_str += str(notebook["Hyperparameter"])
        overleaf_str += " & " 
        overleaf_str += str(notebook["ModelArchitecture"])
        overleaf_str += " & " 
        if notebook["Topic"] == "Predicative Analytics":
            overleaf_str += "PA"
        elif notebook["Topic"] == "Data Analytics":
            overleaf_str += "DA"
        else:
            overleaf_str += notebook["Topic"]
        # overleaf_str += " & " 
        # overleaf_str += notebook["Link"]
        overleaf_str += " \\\\ \n " 
        # overleaf_str += " \hline \n " 
    with open(output_path, 'w') as f:
        f.write(overleaf_str)

data = load_notebooks()
data = read_alt(data, "DataCleaning")
data = read_alt(data, "DataPreprocessing")
data = read_alt(data, "Hyperparameter")
data = read_alt(data, "ModelArchitecture")

data = filter_notebooks(data)
generate_overleaf_table(data, "./output/overleaf_notebook_table.txt")
# print (data)