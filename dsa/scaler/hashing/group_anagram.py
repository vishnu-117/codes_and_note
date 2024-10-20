from collections import defaultdict

def group_anagram(list_of_str):
    anagrams = defaultdict(list)

    for string in list_of_str:
        frequency_array = [0] * 26
        for characher in string:
            frequency_array[ord(characher) - ord('a')] += 1
        
        key = tuple(frequency_array)
        anagrams[key].append(string)

    return anagrams.values()

strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(group_anagram(strs))


A = "abc"
B = "abcbacabc"

A = "aca"
B = "acaa"
# a_len = 
next_pointer = len(A)
result = 0

a_frequency = defaultdict()

def frequency_arr_of_A(A):
    tmp_frequcny_arr = [0] * 26
    for char in A:
        tmp_frequcny_arr[ord(char)-ord('a')] += 1
    
    key = tuple(tmp_frequcny_arr)
    a_frequency[key] = 1

def count_anagram(string):
    tmp_frequency_arr = [0] * 26
    for char in string:
        tmp_frequency_arr[ord(char) - ord('a')] += 1
    
    key = tuple(tmp_frequency_arr)

    if key in a_frequency:
        return 1
    return 0

frequency_arr_of_A(A)
for index in range(0, len(B)):

    if next_pointer > len(B):
        print(next_pointer, 'pointer')
        break
    sub_string = B[index: next_pointer]
    result += count_anagram(sub_string)
    next_pointer += 1
    print(sub_string)
    print(index)

print(result, 'result')
