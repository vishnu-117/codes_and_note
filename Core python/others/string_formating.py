mapping = {
    '10': 'A',
    '11': 'B',
    '12': 'C',
    '13': 'D',
    '14': 'E',
    '15': 'F'
}

def convert_dec_to_hexa(number):
    if number < 16:
        if mapping.get(str(number)):
            return mapping.get(str(number))
        return str(number)
    # elif number % 16 == 0:
    #     return str(10 * (number // 16))
    else:
        reminder = str(number % 16)
        if not mapping.get(reminder) is None:
            reminder = mapping.get(reminder)
        final_result = reminder + convert_dec_to_hexa(number // 16)
    return final_result

def convert_dec_to_octal(number):
    if number < 8:
        return str(number)
    # elif number % 8 == 0:
    #     return str(10* (number // 8))
    else:
        final_result = str(number % 8) + convert_dec_to_octal(number // 8)
    return final_result

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
    l1 = len(bin(number)[2:])
    for i in range(1, number+1):
        print(str(i).rjust(l1,' '),end=" ")
        print(convert_dec_to_octal(i)[::-1].rjust(l1,' '),end=" ")
        print(convert_dec_to_hexa(i)[::-1].rjust(l1,' '),end=" ")
        print(convert_dec_to_binary(i)[::-1].rjust(l1,' '),end=" ")
        print("")

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
