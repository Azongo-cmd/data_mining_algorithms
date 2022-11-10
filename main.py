import csv
import itertools


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

def get_unique_items(dataset: list) -> set:
    result = set()
    for transaction in dataset:
        for item in transaction:
            result.add(item)
    return [set(item) for item in list(result)] 

def count_items(item: set, dataset: list) -> int:
    total = 0
    for transaction in dataset:
        if item.issubset(transaction):
            total +=1
    return total

def get_total_items(dataset:list) -> int:
    return len(dataset)

def frequent_itemset(previous_candidate: list, actual_canditate: list,min_support: int, dataset) -> list:
    result = []
    if previous_candidate == []:
        for item in actual_canditate:
            if count_items(item, dataset) >= min_support:
                result.append(item)
    else:
        """
        for item in actual_candidate
         - get all subset of the item
         - if all subset exist in the previous candidate, count and compare with the min_support
         - else it can't be a frequent item
        """
        for item in actual_canditate:
            item_subsets = get_subsets(item, len(previous_candidate[0]))
            if is_all_subset_exist(previous_candidate, item_subsets):
                if count_items(item, dataset) >= min_support:
                    result.append(item)
    return result

def get_subsets(item, subset_size):
    return [set(subset) for subset in itertools.combinations(item, subset_size)]

def is_all_subset_exist(candidate, subsets):
    for subset in subsets:
        if subset not in candidate:
            return False
    return True

def generate_candidate(previous_candidate:list)-> list:
    result = []
    size =  len(previous_candidate[0]) + 1
    for i in range(len(previous_candidate)):
        set_union = set()
        for j in range(i, len(previous_candidate)):
            set_union = previous_candidate[i].union(previous_candidate[j])
            for subset in itertools.combinations(set_union, size):
                result.append(set(subset))

    return result

def apriori_principle(dataset, min_support) -> list:
    result = []
    previous_candidate = []
    actual_candidate = get_unique_items(dataset) 
    previous_candidate = frequent_itemset(previous_candidate,actual_candidate,min_support, dataset)
    result.append(previous_candidate)
    while previous_candidate != []:
        actual_candidate = generate_candidate(previous_candidate)
        previous_candidate = frequent_itemset(previous_candidate, actual_candidate, min_support, dataset)
    return result
#print(get_unique_items([['a', 'b'], ['a','d','e']]))
data = get_data('test.csv')
print(apriori_principle(data, 3))