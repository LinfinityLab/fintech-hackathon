import os
import csv
import json

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
file_path = os.path.join(BASE_DIR, "static/dataset/all.csv")

def parsing():
    my_dict = {}
    with open(file_path, 'r') as csvfile:
        reader = csv.reader(csvfile)
        reader.next()
        for row in reader:
            my_dict[row[1]] = row[0]

    myjson = json.dumps(my_dict, ensure_ascii=False)

    with open("data.json", 'w') as jsonfile:
        jsonfile.write(myjson)

parsing()
