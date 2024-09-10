def solve(self, A):
    result = 0

    def sum(A):
        nonlocal result
        if A % 10 == 0:
            return A // 10
        else:
            result += A%10
            sum(A//10)
            return result

    result = sum(A)
            
    return 0