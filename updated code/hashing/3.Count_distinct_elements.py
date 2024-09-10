def distinct(arr, l):
    """
    TC: O(n), SC: O(n)
    """
    S = set()
    for i in range(l):
        S.add(arr[i])

    ans = len(S)
    return ans


if __name__ == '__main__':
    arr = [12, 10, 9, 45, 2, 10, 10, 45]
    l = len(arr)

    dis_elements = distinct(arr, l)
    print(dis_elements, "")
