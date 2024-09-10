array = '4 1 2 3 4'
# print(array, type(array))
len_of_array = array[0]
new_array = array[2:]
number_to_rotate = 2
for j in range(number_to_rotate):
    # import pdb; pdb.set_trace()
    new_array = new_array[-1] +' '+new_array[:len(new_array)-1].strip()
    # import pdb; pdb.set_trace()
print(new_array)