a = 2
b = 3

def calculate_power(a, b):
    # print(b)
    if b == 0:
        return 1
    else:
        return a * calculate_power(a, b-1)

print(calculate_power(a, b))