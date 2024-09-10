# take second element for sort
def sort_with_second_number(data):
    # import ipdb
    # ipdb.set_trace()
    return data[1]
# random list
random = [(2, 2), (3, 4), (4, 1), (1, 3)]

# sort list with key
random.sort(key=sort_with_second_number)
# print list
print('Sorted list:', random)
