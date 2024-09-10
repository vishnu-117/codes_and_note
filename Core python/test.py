#!/bin/python3

import math
import os
import random
import re
import sys
from traceback import print_tb



#
# Complete the 'maxDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY px as parameter.
#

def maxDifference(px):
    result = 0
    length = len(px)
    # import pdb; pdb.set_trace()
    for i in range(length-1, -1, -1):
        # print(i, 'ii')
        for k in range(i, -1, -1):
            # print( px[i], px[k], ',,,')
            if px[i] > px[k] and (px[i] - px[k] > result):
                print(px[i], px[k])
                result = px[i] - px[k]
    return result
                
        

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # px_count = int(input().strip())

    # px = []

    # for _ in range(px_count):
    #     px_item = int(input().strip())
    #     px.append(px_item)
    px = [2, 3, 10, 2, 4, 8, 1]
    result = maxDifference(px)
    print(result)
    # fptr.write(str(result) + '\n')

    # fptr.close()
