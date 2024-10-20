def partation(A, start, end):
    pivot = A[end]
    partation_index = start

    for i in range(start, end):
        if A[i] <= pivot:
            A[i], A[partation_index] = A[partation_index], A[i]
            partation_index += 1

    A[partation_index], A[end]= A[end], A[partation_index]
    return partation_index

def quick_sort(A, start, end):
    if start < end:
        partation_index = partation(A, start, end)
        quick_sort(A, start, partation_index-1)
        quick_sort(A, partation_index+1, end)
    return A

arr = [0,3,1,5,2]
print(quick_sort(arr, 0, 4))
