import string

alphabet = set(string.ascii_lowercase)
# print(alphabet)
# print(string.ascii_lowercase)


def ispangram(str):
    print(set(alphabet) - set(str))
    return not set(alphabet) - set(str)


# Driver code
string = "the quick brown fox jumps over the lazy dog"

print(ispangram(string))
