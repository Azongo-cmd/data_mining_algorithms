import csv
from unittest import result

def get_data(filename):
    result = []
    count = 0
    with open(filename) as csvfile:
        csv_reader = csv.reader(csvfile,delimiter=';')
        for row in csv_reader:
            if count == 0:
                count +=1
            else:
                result.append(row[1].strip().split(","))
    return  result



print(get_data('test.csv'))