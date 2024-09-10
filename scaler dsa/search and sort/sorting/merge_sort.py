
def sort(first_half, second_half, A):
    i = 0
    j = 0
    k = 0
    first_half_len = len(first_half)
    second_half_len = len(second_half)
    length = len(A)

    while i < first_half_len and j < second_half_len:
        if first_half[i] < second_half[j]:
            A[k] = first_half[i]
            i += 1
        else:
            A[k] = second_half[j]
            j += 1
        k += 1
    
    while i < first_half_len:
        A[k] = first_half[i]
        i += 1
        k += 1

    while j < second_half_len:
        A[k] = second_half[j]
        j += 1
        k += 1
    
    return A

def merge_sort(A):
    lenght = len(A)
    if lenght < 2:
        return
    mid = lenght // 2
    first_half = A[:mid]
    second_haf = A[mid:]
    merge_sort(first_half)
    merge_sort(second_haf)
    result = sort(first_half, second_haf, A)
    return result

arr = [1,3,8,2,5]
arr = [12, 12, 23, 4 , 6, 6, 10, -35, 28]
print(merge_sort(arr))