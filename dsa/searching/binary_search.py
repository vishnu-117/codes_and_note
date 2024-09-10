def binarySearch(arr, number):
    start = 0
    end = len(arr) - 1
    found = False
    while start <= end:
        mid = (start + end) // 2
        if arr[mid] == number:
            found = True
            break
        elif number > arr[mid]:
            start = mid + 1
        else:
            end = mid - 1
    return found


print(binarySearch([1, 2, 3, 4, 5, 11, 20, 50, 80, 100], 0))

