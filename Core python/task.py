# data = [('Veg Biryani', 'Biryani'), ('Chicken Biryani', 'Biryani'), ('Egg Roll', 'Rolls'), ('Paneer wrap', 'Rolls'), ('Chicken Manchow Soup', 'Soup'), ('Egg Biryani', 'Biryani')]

# result = {}

# for i in data:
#   if i[1] in result.keys():
#     result[i[1]].append(i[0])
#   else:
#     initial_data = []
#     initial_data.append(i[0])
#     result[i[1]] = initial_data

# for key, value in result.items():
#   result[key].sort()
# print(result)

# color = namedtuple('count',['biryani', 'rolls', 'blue'])

# color(['1', '2','3'])
data ={
  '1':['',],
  '2':['a', 'b', 'c'],
  '3':['d', 'e', 'f'],
  '4':['g', 'h', 'i'],
  '5':['j', 'k', 'l'],
  '6':['m', 'n', 'o'],
  '7':['p', 'q', 'r', 's'],
  '8':['t', 'u', 'v'],
  '9':['w', 'x', 'y', 'z'],
  '0':[' ',],
}

# 2222 -> ca
# string = '2222'
string = '12345'

count = 0
result = ''
lenght = len(string)
for index in range(lenght):
    print(index, 'index')
    if index == lenght-1:
        # import pdb; pdb.set_trace()
        if string[index] == string[index-1]:
            count += 1
        elif count == 0:
            count += 1
    is_count = False
    if index != lenght-1 and string[index] == string[index+1]:
        is_count = True

    if (is_count and count < 3 and not string[index] in ['7', '9']) or (is_count and count < 4  and string[index] in ['7', '9']) :
        count += 1
        print(count, index, 'ifffff')
    else:
        if is_count is False:
            count = 1
        print(count, index, 'elseee')
        result += data[string[index]][count-1]
        count = 0
    if (is_count and count == 3 and not string[index] in ['7', '9']) or (is_count and count == 4  and string[index] in ['7', '9']):
        print(count, index, 'last last')
        result += data[string[index]][count-1]
        count = 0


# def func(string, count=0):
#   if 
#   result = func()
print(result)
  
  