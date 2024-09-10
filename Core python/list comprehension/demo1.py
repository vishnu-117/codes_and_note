my_list = []
for i in "abcd":
    for num in range(4):
        my_list.append((i, num))
my_list1 = [[i, j] for i in "abcd" for j in range(4)]
print(my_list1)
