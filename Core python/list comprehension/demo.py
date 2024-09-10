num = [1, 2, 3, 4, 5, 6, 7, 8]
# my_list = [i for i in num if i % 2 == 0]
# my_list = map(lambda x: x * x, num)
my_list = filter(lambda x: x % 2 == 0, num)
print(my_list)
