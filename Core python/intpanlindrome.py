def intpalindrome(number):
    palindrome = number
    reverse = 0

    while number != 0:
        remainder = number % 10
        reverse = reverse * 10 + remainder
        number = number // 10

    if palindrome == reverse:
        return True
    else:
        return False


print(intpalindrome(1221))
