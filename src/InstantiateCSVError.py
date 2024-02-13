import csv
import pathlib


class InstantiateCSVError(Exception):
    def __init__(self):
        pass

    def __str__(self):
        return "Файл item.csv поврежден"