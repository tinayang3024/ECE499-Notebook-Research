import pymongo
from pymongo import MongoClient
import os

# this script pulls a list of existing attributes in the mongodb database for each type of changes

# input
output_path = "./new_cv"


# script
cluster = MongoClient("mongodb+srv://research:research@kagglenotebookanalysis.lbykx.mongodb.net/test")
db = cluster["NotebookAlternatives"]

data_prepro = []
data_cleaning = []
model_arc = []
hyperparameter = []
collection = db["DataPreprocessing"]
results = collection.find({})
for res in results:
    data_prepro.append(res["description"])

collection = db["DataCleaning"]
results = collection.find({})
for res in results:
    data_cleaning.append(res["description"])

collection = db["Hyperparameter"]
results = collection.find({})
for res in results:
    hyperparameter.append(res["description"])

collection = db["ModelArchitecture"]
results = collection.find({})
for res in results:
    model_arc.append(res["description"])

data_prepro = list(set(data_prepro))
data_cleaning = list(set(data_cleaning))
hyperparameter = list(set(hyperparameter))
model_arc = list(set(model_arc))

data_prepro_file = output_path + "/data_preprocessing_new.csv"
data_cleaning_file = os.path.join(output_path, "data_cleaning_new.csv")
hyperparameter_file = os.path.join(output_path, "hyperparameter_new.csv")
model_arc_file = os.path.join(output_path, "model_arc_new.csv")
with open(data_prepro_file, 'w') as f:
    for line in data_prepro:
        f.write(line + ", \n")
        f.write(",\n")
# with open(data_cleaning_file, 'w') as f:
#     for line in data_cleaning:
#         f.write(line + ", \n")
# with open(hyperparameter_file, 'w') as f:
#     for line in hyperparameter:
#         f.write(line + ", \n")
# with open(model_arc_file, 'w') as f:
#     for line in model_arc:
#         f.write(line + ", \n")
