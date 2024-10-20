ini_list = [
    {"name": "akash", "d.o.b": "1997-03-02"},
    {"name": "manjeet", "d.o.b": "1997-01-04"},
    {"name": "nikhil", "d.o.b": "1997-09-13"},
]

# ini_list.sort(key=lambda x: x["d.o.b"])
a = sorted(ini_list, key=lambda x: x["d.o.b"], reverse=True)
print(a)

