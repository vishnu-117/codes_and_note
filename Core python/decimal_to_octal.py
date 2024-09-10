def convert_dec_to_octal(number, result=''):
    if number < 8:
        return str(number)
    elif number % 8 == 0:
        return str(10* (number // 8))
    else:
        final_result = str(number % 8) + convert_dec_to_octal(number // 8, result)
    return final_result

def print_formatted(number):
    result = convert_dec_to_octal(number, result='')
    return result[::-1]

if __name__ == '__main__':
    n = 127
    print(print_formatted(n))
