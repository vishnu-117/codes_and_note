def remoteItem(mydict):
    newdict = {key: value for key, value in mydict.items() if key != "Mani"}
    print(newdict)


a = {"Arushi": 22, "Anuradha": 21, "Mani": 21, "Haritha": 21}
remoteItem(a)
