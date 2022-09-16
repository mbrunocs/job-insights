from functools import lru_cache
import csv


@lru_cache
def read(path):
    lista = list()
    with open(path, mode="r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            lista.append(row)
    return lista
