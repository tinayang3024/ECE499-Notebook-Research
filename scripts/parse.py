import pymongo
from pymongo import MongoClient

cluster = MongoClient("mongodb+srv://research:research@kagglenotebookanalysis.lbykx.mongodb.net/test")
db = cluster["NotebookAlternatives"]
# collection = db["DataPreprocessing"]
# collection = db["Hyperparameter"]
# collection = db["ModelArchitecture"]

# fp = "./notebook_data.csv"
# with open(fp, 'r') as f:
#     print("hi")
#     des = ''
#     others = []
#     file = []
#     for line in f:
#         file.append(line)
#     for i in range(len(file)):
#         line = file[i]
#         if i <= 4:
#             continue
#         notebook_id = line.split(",")
#         t = (i-4)%3
#         # print("t:", t)
#         # print (notebook_id)
#         if t != 0:
#             continue
#         version_id = file[i+1].split(",")
#         line_number = file[i+2].split(",")

#         des = notebook_id[0]
#         j = 1        
#         while notebook_id[j] != '':
#             data = {}
#             data["description"] = des
#             data["Notebook ID"] = notebook_id[j]
#             data["Version ID"] = version_id[j]
#             data["Line Number"] = line_number[j]
#             j += 1
#             if j > len(notebook_id) or notebook_id[j] == "\n":
#                 break
#             print("data: ", data)
#             collection.insert_one(data)
#         # print (notebook_id)

# fp = "./hyperparameter.csv"
fp = "./model_architecture.csv"
with open(fp, 'r') as f:
    for line in f:
        words = line.split(",")
        des = words[0]
        if des == "":
            break
        for i in range(1,len(words)):
            if words[i] == "\n" or words[i] == "":
                continue
            data = {}
            data["description"] = des
            data["Notebook ID"] = words[i]
            print("data: ", data)
            collection.insert_one(data)
# collection.insert_one(data)
