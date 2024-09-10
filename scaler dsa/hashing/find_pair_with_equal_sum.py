

def find_pairs_with_equal_sum(arr):
    sum_dict = {}

    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            current_sum = arr[i] + arr[j]

            if current_sum in sum_dict:
                (index1, index2) = sum_dict[current_sum]
                return (i,j),(index1, index2)

            sum_dict[current_sum] = (i,j)

arr = [3, 4, 7, 1, 2, 9, 8]
result = find_pairs_with_equal_sum(arr)

if result:
    (a,b), (c,d) = result
    print('first pair index', (a,b), 'second pair index', (c,d))