import pymongo
from pymongo import MongoClient
import numpy as np
import matplotlib.pyplot as plt

cluster = MongoClient("mongodb+srv://research:research@kagglenotebookanalysis.lbykx.mongodb.net/test", )
db = cluster["NotebookAlternatives"]
collection = db["ModelArchitecture"]
# collection = db["Hyperparameter"]
# collection = db["DataPreprocessing"]
results = collection.find({})
# print("results")
counter = {}
for res in results:
    print(res)
    if not res["description"] in counter.keys():
        counter[res["description"]] = 1
    else:
        counter[res["description"]] += 1


counter = dict(sorted(counter.items(), key=lambda item: item[1], reverse=True))
courses = list(counter.keys())
values = list(counter.values())
fig = plt.figure(figsize = (10, 5))
# fig = plt.figure(figsize = (8, 10))


#  Bar plot
plt.barh(courses, values, align='center')
plt.xlabel("Number of Notebooks", fontsize=10)
plt.ylabel("Changes", fontsize=10)
plt.title("Model Architecture")
plt.show()
fig.tight_layout()
fig.savefig('ModelArchitecture.jpg')
# ========================================================

# collection = db["ModelArchitecture"]
collection = db["Hyperparameter"]
# collection = db["DataPreprocessing"]
results = collection.find({})
# print("results")
counter = {}
for res in results:
    print(res)
    if not res["description"] in counter.keys():
        counter[res["description"]] = 1
    else:
        counter[res["description"]] += 1


counter = dict(sorted(counter.items(), key=lambda item: item[1], reverse=True))
courses = list(counter.keys())
values = list(counter.values())
# fig = plt.figure(figsize = (10, 5))
fig = plt.figure(figsize = (8, 10))


#  Bar plot
plt.barh(courses, values, align='center')
plt.xlabel("Number of Notebooks", fontsize=10)
plt.ylabel("Changes", fontsize=10)
plt.title("Hyperparameter")
plt.show()
fig.tight_layout()
fig.savefig('Hyperparameter.jpg')

# ========================================================
# collection = db["ModelArchitecture"]
# collection = db["Hyperparameter"]
collection = db["DataPreprocessing"]
results = collection.find({})
# print("results")
counter = {}
for res in results:
    print(res)
    if not res["description"] in counter.keys():
        counter[res["description"]] = 1
    else:
        counter[res["description"]] += 1


counter = dict(sorted(counter.items(), key=lambda item: item[1], reverse=True))
courses = list(counter.keys())
values = list(counter.values())
# fig = plt.figure(figsize = (10, 5))
fig = plt.figure(figsize = (8, 10))


#  Bar plot
plt.barh(courses, values, align='center')
plt.xlabel("Number of Notebooks", fontsize=10)
plt.ylabel("Changes", fontsize=10)
plt.title("Data Preprocessing")
plt.show()
fig.tight_layout()
fig.savefig('DataPreprocessing.jpg')
