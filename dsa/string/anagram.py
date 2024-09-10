def isanagram(str1, str2):
    if "".join(sorted(str1)) == "".join(sorted(str2)):
        return True
    return False


print(isanagram("listen", "silent"))

