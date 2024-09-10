import pdb


def selectionSort(array):
    # for i in range(len(array) - 1):
    #     min = array[i]
    #     for j in range(i + 1, len(array)):
    #         if min > array[j]:
    #             min = array[j]
    #             temp = array[i]
    #             array[i] = array[j]
    #             array[j] = temp
    for i in range(len(array) - 1):
        min = i
        for j in range(i + 1, len(array)):
            if array[min] > array[j]:
                # min = j
                temp = array[i]
                array[i] = array[j]
                array[j] = temp
        # array[min], array[i] == array[i], array[min]
    return array


array = [1, 5, 8, 2, 10, 20, 7, 9]
# array = [1, 2, 3, 4, 5]
# array = [2, 1, 5, 10, 9]
print(selectionSort(array))

