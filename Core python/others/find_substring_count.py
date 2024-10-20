def is_substring_exists(current_idx, string, sub_string):
    sub_str_len = len(sub_string)
    if len(string[current_idx:]) >=sub_str_len:
        str1 = string[current_idx:current_idx+sub_str_len]
        import pdb; pdb.set_trace()
        if str1 == sub_string:
            # import pdb; pdb.set_trace()
            return True
        else:
            return False

def count_substring(string, sub_string):
    count = 0
    for idx, char in enumerate(string):
        if char==sub_string[0]:
            if is_substring_exists(idx, string, sub_string) is True:
                count += 1
    return count
    

if __name__ == '__main__':
    print(count_substring('ABCDCDC', 'CDC'))
    # string = raw_input().strip()
    # sub_string = raw_input().strip()
    
    # count = count_substring(string, sub_string)
    # print count