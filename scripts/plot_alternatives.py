
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

def print_stat(type_, data):
    print("type: " + str(type_))
    for topic, counter in data.items():
        print("topic: " + topic)
        sum_ = 0
        for key, val in counter.items():
            sum_ += val
        print("count: " + str(sum_))
        print("----------------------")
    print("==========================")

def print_most_freq(type_, data):
    print("type: " + str(type_))
    for topic, counter in data.items():
        print("topic: " + topic)
        sorted_counter = dict(sorted(counter.items(), key=lambda item: item[1], reverse=True))
        i = 0
        for key, val in sorted_counter.items():
            i += 1
            if i > 3:
                break
            print("key: " + str(key))
        print("----------------------")
    print("==========================")

def plot_seperate_alt(type_, data):
    for topic, counter in data.items():
        courses = list(key[:20] + "..." if len(key) > 20 else key for key in counter.keys())
        values = list(counter.values())
        fig = plt.figure(figsize = (8, 10))
        plt.barh(courses, values, align='center')
        plt.xlabel("Number of Notebooks", fontsize=20)
        plt.ylabel("Changes", fontsize=20)
        plt.yticks(fontsize=15)
        plt.title(topic + ": " + type_,  fontsize=20)
        plt.show()
        fig.tight_layout()
        fig.savefig(os.path.join(output_path, '{}.jpg'.format(topic + "_" + type_)))

print("**** Start Loading Notebooks ****")
notebookinfo = load_notebooks()

print("**** Start Loading Alternatives ****")
alt_ma = load_alternatives("ModelArchitecture", notebookinfo)
alt_h = load_alternatives("Hyperparameter", notebookinfo)
alt_dp = load_alternatives("DataPreprocessing", notebookinfo)
alt_c = load_alternatives("DataCleaning", notebookinfo)

# print("**** Start Printing Stats ****")
# print_stat("ModelArchitecture", alt_ma)
# print_stat("Hyperparameter", alt_h)
# print_stat("DataCleaning", alt_c)
# print_stat("DataPreprocessing", alt_dp)

# print("**** Start Printing Stats ****")
# print_most_freq("ModelArchitecture", alt_ma)
# print_most_freq("Hyperparameter", alt_h)
# print_most_freq("DataCleaning", alt_c)
# print_most_freq("DataPreprocessing", alt_dp)

# print("**** Start Plotting Alternatives ****")
plot_seperate_alt("ModelArchitecture", alt_ma)
plot_seperate_alt("Hyperparameter", alt_h)
plot_seperate_alt("DataCleaning", alt_c)
plot_seperate_alt("DataPreprocessing", alt_dp)