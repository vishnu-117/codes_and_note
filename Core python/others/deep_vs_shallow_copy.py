import copy

old_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
new_list = copy.copy(old_list)
new_list[0][0] = 'AA'
new_list.append(['new'])
print("Old list:", old_list, id(old_list))
print("New list:", new_list, id(new_list))




old_list = [[1, 1, 1], [2, 2, 2], [3, 3, 3]]
new_list = copy.deepcopy(old_list)

old_list[1][0] = 'BB'

print("Old list:", old_list)
print("New list:", new_list)