
from pymongo import MongoClient

cluster = MongoClient("mongodb+srv://research:research@kagglenotebookanalysis.lbykx.mongodb.net/test", )
db = cluster["NotebookAlternatives"]
output_path = "./output/"



collection = db["DataPreprocessing"]
collectionPre = db["DataPreprocessing"]
collectionBackUp = db["backup"]
collectionClean = db["DataCleaning"]
results = collectionBackUp.find({})
# alt = []
# for res in results:
#     # print(res["description"])
#     alt.append(res["description"])

# alt = list(set(alt))
# print (alt)

dataClean = ['Remove Emoji', 'Remove Punctuations','Remove Constant Features', 'Drop unrelated features', 'Remove HTML tags', 'Fill missing data', 'Filter non-string words', 'Convert Image Size', 'Spelling Correction', 'Remove Duplicate Columns/Data', 'Drop Sparse Data','Break down timestamp data']
dataPre = ['Filter Stopwords', 'Remove Outliers', 'Add one-hot feature', 'Create model to generate meta data', 'Data Smoothing based on mean', 'Data Aggregation (Include Mean/Avg/Max/Min/Med/Sum)', 'Round Data','Concat strings (e.g. trigram)', 'Introduce new features based on existing features', 'Include Var Rank']


for res in results:
    print (res)
    data = {}
    data["description"] = res["description"]
    data["Notebook ID"] = res["Notebook ID"]
    data["Version ID"] = res["Version ID"]
    data["Line Number"] = res["Line Number"]
    # collectionBackUp.insert_one(data)
    if res["description"] in dataClean:
        collectionClean.insert_one(data)
    if res["description"] in dataPre:
        collectionPre.insert_one(data)
