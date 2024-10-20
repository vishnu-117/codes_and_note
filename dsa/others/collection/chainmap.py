from collections import ChainMap

# Python code to demonstrate ChainMap and
# new_child()

import collections

# initializing dictionaries
dic1 = { 'a' : 1, 'b' : 2 }
dic2 = { 'b' : 3, 'c' : 4 }
dic3 = { 'f' : 5 }

# initializing ChainMap
chain = ChainMap(dic1, dic2)

# printing chainMap
print ("All the ChainMap contents are : ")
print (chain)

# using new_child() to add new dictionary
chain1 = chain.new_child(dic3)

# printing chainMap
print ("Displaying new ChainMap : ")
print (chain1)
