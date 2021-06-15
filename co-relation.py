import plotly_express as px
import csv
import numpy as np

def getDataSource(data_path):
    marks = []
    rollnum = []
    with open(data_path) as f:
        csv_reader = csv.DictReader(f)
        for row in csv_reader:
            marks.append(float(row["Marks In Percentage"]))
            rollnum.append(float(row["Roll No"]))
    return{"x":marks,"y":rollnum}

def findcorelation(dataSource):
    corelation = np.corrcoef(dataSource["x"],dataSource["y"])
    print("corelation is",corelation[0,1])

def setup():
    dataPath = "data1.csv"
    dataSource = getDataSource(dataPath)
    findcorelation(dataSource)

setup()