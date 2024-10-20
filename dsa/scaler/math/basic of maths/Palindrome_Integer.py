def isPalindrome(A):
    new_number = 0
    c = abs(A)
    A = abs(A)
    
    while A != 0:
        mod = A % 10
        new_number = new_number * 10 + mod
        A = A//10
        
    if new_number ==  c:
        return True
    else:
        return False

# number = 1321
number = -2147447412
print(isPalindrome(number))