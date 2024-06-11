import random

def FindMax(lst):
    if not lst:
        return None
    
    max_value = lst[0]
    for element in lst:
        if element > max_value:
            max_value = element
    return max_value

def TidyListDict(lst, key):
    return sorted(lst, key=lambda x: x[key])

def ReverseList(lst):
    return lst[::-1]

def CountOccurrence(lst, element):
    return lst.count(element)

def DeleteDuplicates(lst):
    return list(set(lst))

def MergeLists(lst1, lst2):
    return list(dict.fromkeys(lst1 + lst2))

def CreateMap(keys, values):
    if len(keys) != len(values):
        raise ValueError("Keys and values lists must have the same length.")
    return dict(zip(keys, values))

def AddIfUnique(lst, element):
    if element not in lst:
        lst.append(element)
    return lst

def FilterList(lst, filter_function):
    return list(filter(filter_function, lst))

def ApplyFunction(lst, function):
    return list(map(function, lst))

def ShuffleList(lst):
    random.shuffle(lst)
    return lst

def GenerateRandomList(length, start, end):
    return [random.randint(start, end) for _ in range(length)]

def SplitList(lst, n):
    return [lst[i:i + n] for i in range(0, len(lst), n)]
