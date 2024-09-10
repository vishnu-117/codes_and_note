def mergesort(number):
    if len(number) > 1:
        mid = len(number) // 2
        left = number[:mid]
        right = number[mid:]
        mergesort(left)
        mergesort(right)

        i = j = k = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                number[k] = left[i]
                i += 1
                k += 1
            else:
                number[k] = right[j]
                j += 1
                k += 1
        while i < len(left):
            number[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            number[k] = right[j]
            j += 1
            k += 1
    print(number)


arr = [12, 10, 8, 13, -9, 17]
mergesort(arr)
