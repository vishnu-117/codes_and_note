def mergeTwoDict(dict1, dict2):
    dict1.update(dict2)
    print(dict1)
    new_dict = {**dict1, **dict2}
    print(new_dict)


dict1 = {"a": 10, "b": 20}
dict2 = {"c": 30, "d": 40, "b": 20}

mergeTwoDict(dict1, dict2)

