# Given a list of numbers and a number k, return whether
#  any two numbers from the list add up to k.

# For example, given [10, 15, 3, 7] and k of 17,
# return true since 10 + 7 is 17.


def twonumbersum(numbers, k):
    result = [
        [True for j in range(len(number))] for i in range(len(number)) if j + i == k
    ]
    print(result)


number = [10, 15, 3, 7]
k = 17
twonumbersum(number, k)
