import re


def isStrContainSpecialChar(str):
    regex = re.compile("[!@#$%^&*()?]")
    if regex.search(str) == None:
        print("special character is not present in str")
    else:
        print("special character is present in string")


isStrContainSpecialChar("GeeksForGeeks")
