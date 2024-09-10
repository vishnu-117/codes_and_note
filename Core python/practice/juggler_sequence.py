#code
import math
T = 3
# list1 = []
# for i in range(1):
number = 14
while number >1:
    # import pdb;pdb.set_trace()
    if number % 2 == 0:
        number = int((number)**0.5)
        # list1.append(number)
        # print(number,end=" ")
    else:
        number = math.floor((number)**(3/2))
        # list1.append(number)
        # print(number)
    print(number,end=' ')