result = []
stack = []
def paren(n):
    def backtract(Open, Close):
        if Open == Close == n:
            result.append("".join(stack))
            return
        
        if Open < n:
            stack.append('(')
            backtract(Open + 1, Close)
            stack.pop()
        
        if Close < Open:
            stack.append(')')
            backtract(Open, Close + 1)
            stack.pop()
    backtract(0, 0)
    return result

n = 2
print(paren(n))