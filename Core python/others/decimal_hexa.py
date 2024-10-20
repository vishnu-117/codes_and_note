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
    elif number % 16 == 0:
        return str(10 * (number // 16))
    else:
        reminder = str(number % 16)
        import pdb; pdb.set_trace()
        if not mapping.get(reminder) is None:
            reminder = mapping.get(reminder)
        final_result = reminder + convert_dec_to_hexa(number // 16)
    return final_result

def print_formatted(number):
    l1 = len(bin(number)[2:])
    result = convert_dec_to_hexa(number)
    return result[::-1].rjust(l1, ' ')

if __name__ == '__main__':
    n = 9
    print(print_formatted(n))
