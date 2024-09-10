"""
Example Usage Summary:
Append: Adds an item to the end.
Extend: Appends elements from an iterable.
Insert: Adds an item at a specific position.
Remove: Deletes the first occurrence of an item.
Pop: Removes and returns an item at a specific position.
Clear: Empties the list.
Index: Finds the first occurrence of an item.
Count: Counts the occurrences of an item.
Sort: Orders the list in place.
Reverse: Reverses the list in place.
Copy: Creates a shallow copy of the list.

lst = [1, 2, 3]
lst.append(4)
# lst: [1, 2, 3, 4]


lst = [1, 2]
lst.extend([3, 4])
# lst: [1, 2, 3, 4]

lst = [1, 2, 4]
lst.insert(2, 3)
# lst: [1, 2, 3, 4]

lst = [1, 2, 3, 2]
lst.remove(2)
# lst: [1, 3, 2]

lst = [1, 2, 3]
item = lst.pop()
# lst: [1, 2]
# item: 3

lst = [1, 2, 3]
lst.clear()
# lst: []

lst = [1, 2, 3, 2]
index = lst.index(2)
# index: 1


lst = [1, 2, 3, 2]
count = lst.count(2)
# count: 2

lst = [3, 1, 2]
lst.sort()
# lst: [1, 2, 3]

lst = [1, 2, 3]
lst.reverse()
# lst: [3, 2, 1]

lst = [1, 2, 3]
copied_lst = lst.copy()
# copied_lst: [1, 2, 3]


"""