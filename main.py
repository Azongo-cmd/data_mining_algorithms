import csv


def get_data(filename:str) -> list:
    result = []
    count = 0
    with open(filename) as csvfile:
        csv_reader = csv.reader(csvfile,delimiter=';')
        for row in csv_reader:
            if count == 0:
                count +=1
            else:
                result.append(set(row[1].strip().split(",")))
    return  result

def get_unique_items(dataset: list) -> list:
    result = set()
    for transaction in dataset:
        for item in transaction:
            result.add(item)
    return result 

def count_items(item: set, dataset: list) -> int:
    total = 0
    for transaction in dataset:
        if item.issubset(transaction):
            total +=1
    return total

def get_total_items(dataset:list) -> int:
    total = 0
    for transaction in dataset:
        total += len(transaction)
    return  total


print(get_unique_items([['a', 'b'], ['a','d','e']]))