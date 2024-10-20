#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'countSignals' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY frequencies
#  2. 2D_INTEGER_ARRAY filterRanges
#

def countSignals(frequencies, filterRanges):
    # Write your code here
    count = 0
    
    for i in frequencies:
        k = 0
        
        for j in filterRanges:
            # import pdb; pdb.set_trace()
            if i in range(j[0], j[1]+1):
               k += 1 
        import pdb ; pdb.set_trace()
        if k == len(filterRanges[0]):
            count += 1

    return count
# if __name__ == '__main__':

print(countSignals([5,20,5,6,7,12,3,2], [[10,20],[5,15],[5,30]]))