from collections import OrderedDict

d = {}
d['a'] = 1
d['b'] = 2
d['c'] = 3
d['d'] = 4
   
for key, value in d.items():
    print(key, value)

d = OrderedDict()
d['a'] = 1
d['b'] = 2
d['c'] = 3
d['d'] = 4

print('------------------------')
for key, value in d.items():
    print(key, value)
