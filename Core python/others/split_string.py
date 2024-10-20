import textwrap

def wrap(string, max_width):
    print(len(string))
    for i in range(0, len(string), max_width):
        # try:
        print(i, i+max_width)
        print(string[i:i+max_width])
    return ''
        # except:
            # print(string[i:])

if __name__ == '__main__':
    string, max_width = "ABCDEFGHIJKLIMNOQRSTUVWXYZ", 4
    result = wrap(string, max_width)
    print(result)