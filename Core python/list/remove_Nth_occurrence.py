"""
Given a list of words in Python, the task is to remove the Nth occurrence of the given word in that list.

Examples:

Input: list - ["geeks", "for", "geeks"]
       word = geeks, N = 2
Output: list - ["geeks", "for"]

Input: list - ["can", "you",  "can", "a", "can" "?"]
       word = can, N = 1
Output: list - ["you",  "can", "a", "can" "?"]
"""


def removeNThWord(list, word, N):
    count = 0
    for i in range(0, len(list)):
        if list[i] == word:
            count += 1
            if count == N:
                list.pop(i)
                break
    print(list)


List1 = ["geeks", "for", "geeks"]
List2 = ["can", "you", "can", "a", "can", "?"]
removeNThWord(List1, "geeks", 2)
removeNThWord(List2, "can", 1)
