def convert_dec_to_binary(number):
    if number <= 0:
        return ''
    else:
        if number % 2 == 0:
            str1 = '0'
        else:
            str1 = '1'
        final_result = str1 + convert_dec_to_binary(number // 2)
    return final_result

def print_formatted(number):
    result = convert_dec_to_binary(number)
    return result[::-1]

if __name__ == '__main__':
    n = 8
    print(print_formatted(n))
