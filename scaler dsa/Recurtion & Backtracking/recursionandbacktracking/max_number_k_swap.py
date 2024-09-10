
def find_maximum(string, maxn, k, indx):
    """
    Find Maximum number possible by doing at-most K
    """

    n = len(string)

    if k == 0 or indx == n-1:
        return 

    max = string[indx]

    for i in range(indx+1, n):
        if int(string[i]) > int(max):
            max = string[i]

    if string[indx] != max:
        k -= 1
    

    for i in range(indx, n):
        if string[i] == max:
            string[indx], string[i] = string[i], string[indx]

            tmp_str = "".join(string)
            if int(tmp_str) > int(maxn[0]):
                maxn[0] = tmp_str

            find_maximum(string, maxn, k, indx+1)

            string[indx], string[i] = string[i], string[indx]

if __name__ == "__main__":
    string = "999984211"
    maxn = [string]
    k = 4
    indx = 0
    string = [i for i in string]
    find_maximum(string, maxn, k, indx)
    print(maxn[0])
