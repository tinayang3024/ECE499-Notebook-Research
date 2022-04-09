
import pymongo
from pymongo import MongoClient
import numpy as np
import matplotlib.pyplot as plt
import os

cluster = MongoClient("mongodb+srv://research:research@kagglenotebookanalysis.lbykx.mongodb.net/test", )
db = cluster["NotebookAlternatives"]
output_path = "./output/"


def load_notebooks():
    notebooks = {}
    notebooks["NLP"] = []
    notebooks["CV"] = []
    notebooks["Sentiment Analysis"] = []
    notebooks["Data Analytics"] = []
    notebooks["Predicative Analytics"] = []

    collection = db["NotebookInfo"]
    results = collection.find({})
    for res in results:
        notebooks[res['General Topic']].append(res['Notebook ID'])

    for k, v in notebooks.items():
        print(k +"({})".format(len(v)))
    
    return notebooks

def load_alternatives(alt_type, notebookinfo):
    notebook_alt = {}
    notebook_alt["NLP"] = {}
    notebook_alt["CV"] = {}
    notebook_alt["Sentiment Analysis"] = {}
    notebook_alt["Data Analytics"] = {}
    notebook_alt["Predicative Analytics"] = {}

    collection = db[alt_type]
    results = collection.find({})
    for res in results:
        id_ = res["Notebook ID"]

        if id_ in notebookinfo["NLP"]:
            if not res["description"] in notebook_alt["NLP"].keys():
                notebook_alt["NLP"][res["description"]] = 1
            else:
                notebook_alt["NLP"][res["description"]] += 1
        elif id_ in notebookinfo["CV"]:
            if not res["description"] in notebook_alt["CV"].keys():
                notebook_alt["CV"][res["description"]] = 1
            else:
                notebook_alt["CV"][res["description"]] += 1
        elif id_ in notebookinfo["Sentiment Analysis"]:
            if not res["description"] in notebook_alt["Sentiment Analysis"].keys():
                notebook_alt["Sentiment Analysis"][res["description"]] = 1
            else:
                notebook_alt["Sentiment Analysis"][res["description"]] += 1
        elif id_ in notebookinfo["Data Analytics"]:
            if not res["description"] in notebook_alt["Data Analytics"].keys():
                notebook_alt["Data Analytics"][res["description"]] = 1
            else:
                notebook_alt["Data Analytics"][res["description"]] += 1
        elif id_ in notebookinfo["Predicative Analytics"]:
            if not res["description"] in notebook_alt["Predicative Analytics"].keys():
                notebook_alt["Predicative Analytics"][res["description"]] = 1
            else:
                notebook_alt["Predicative Analytics"][res["description"]] += 1
    sorted_alt = {}
    for k, v in notebook_alt.items():
        sorted_alt[k] = dict(sorted(v.items(), key=lambda item: item[1], reverse=True))
    return sorted_alt

def plot_seperate_alt(type_, data):
    for topic, counter in data.items():
        courses = list(counter.keys())
        values = list(counter.values())
        fig = plt.figure(figsize = (8, 10))
        plt.barh(courses, values, align='center')
        plt.xlabel("Number of Notebooks", fontsize=10)
        plt.ylabel("Changes", fontsize=10)
        plt.title(topic + ": " + type_)
        plt.show()
        fig.tight_layout()
        fig.savefig(os.path.join(output_path, '{}.jpg'.format(topic + "_" + type_)))

print("**** Start Loading Notebooks ****")
notebookinfo = load_notebooks()

print("**** Start Loading Alternatives ****")
# alt_ma = load_alternatives("ModelArchitecture", notebookinfo)
# alt_h = load_alternatives("Hyperparameter", notebookinfo)
alt_dp = load_alternatives("DataPreprocessing", notebookinfo)
# alt_c = load_alternatives("DataCleaning", notebookinfo)

# print("**** Start Plotting Alternatives ****")
# plot_seperate_alt("ModelArchitecture", alt_ma)
# plot_seperate_alt("Hyperparameter", alt_h)
# plot_seperate_alt("DataCleaning", alt_c)
plot_seperate_alt("DataPreprocessing", alt_dp)