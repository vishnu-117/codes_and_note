#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'getUmbrellas' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER requirement
#  2. INTEGER_ARRAY sizes
#

def getUmbrellas(requirement, sizes):
    # Write your code here
    size_sum = 0
    count = 0
    for i in sizes:
        if i == requirement:
            return 1
        elif size_sum < requirement:
            size_sum += i
            count += 1
        else:
            pass
            
    if size_sum == requirement:
        return count
    else:
        return -1

# if __name__ == '__main__':
    755

    239

    151

    6

    19

    46

    27

    26

    25

    42

    20

    17

    15

    45

    5

    20

    3

    1

    48

    46

    43

    5

    18

    16

    48

    48

    34

    48

    25

    29

    25

    32

    5

    23

    5

    15

    31

    17

    28

    34

    11

    38

    48

    40

    40

    40

    6

    5

    47

    25

    49

    3

    50

    28

    3

    23

    37

    45

    28

    18

    36

    6

    49

    8

    35

    39

    42

    31

    44

    6

    42

    5

    22

    36

    12

    4

    20

    42

    45

    36

    8

    5

    26

    5

    12

    50

    30

    19

    44

    19

    45

    41

    12

    48

    46

    50

    30

    38

    18

    19

    36

    5

    25

    39

    19

    28

    36

    22

    13

    46

    17

    6

    22

    25

    13

    1

    21

    24

    29

    3

    38

    6

    39

    6

    42

    33

    38

    38

    35

    30

    12

    49

    21

    19

    24

    15

    5

    44

    27

    12

    22

    49

    41

    1

    49

    49

    28

    3

    17

    45

    3

    27

    47

    50

    46

    4

    13

    28

    35

    49

    4

    27

    9

    32

    11

    35

    15

    23

    50

    32

    35

    30

    20

    46

    37

    3

    46

    15

    48

    48

    3

    45

    20

    23

    6

    32

    17

    14

    9

    10

    33

    24

    20

    18

    12

    30

    14

    4

    19

    49

    13

    50

    23

    35

    2

    27

    14

    16

    21

    41

    31

    35

    14

    9

    7

    46

    4

    42

    48

    48

    21

    37

    30

    31

    46

    21

    5

    47

    44

    44

    28

    3

    9

    2

    21

    19

    39

    41

    25

    50

    50