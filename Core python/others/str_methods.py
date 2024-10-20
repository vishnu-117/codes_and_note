import pdb


def true_or_false(func):
    # import pdb; pdb.set_trace()
    if func is True:
        print('True')
    else:
        print('False')
    
if __name__ == '__main__':
    s = input()
    # import pdb; pdb.set_trace()
    true_or_false(s.isalnum())
    true_or_false(s.isalpha())
    # true_or_false(s.isdigit())
    # true_or_false(s.islower())
    # true_or_false(s.isupper())