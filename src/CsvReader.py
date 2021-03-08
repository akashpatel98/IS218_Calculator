import csv
from pprint import pprint


def ClassFactory(class_name, dictionary):
    return type(class_name, (object,), dictionary)


class CSVReader:
    data = []


def __init__(self, filepath):
    with open(filepath):
        csv_data = csv.Dictreader()
        for row in csv_data:
            self.data.append(row)
    pprint(self.data)
    pass
