def instance(para, txt):
    import re
    sample = para
    found = re.findall(txt, sample)
    return len(found)


para = "Nothing lasts... but nothing is lost"
txt = "thing"

print(instance(para, txt))