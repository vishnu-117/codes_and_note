Here are Python solutions for the matrix problems:

---

### 1. **Set Matrix Zeroes**

Given an `m x n` matrix, if an element is `0`, set its entire row and column to zeroes.

#### Solution

```python
def set_zeroes(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    row_zero = False
    col_zero = False
    
    # Check if first row and first column should be zero
    for i in range(rows):
        if matrix[i][0] == 0:
            col_zero = True
    for j in range(cols):
        if matrix[0][j] == 0:
            row_zero = True
    
    # Mark zeros on first row and column
    for i in range(1, rows):
        for j in range(1, cols):
            if matrix[i][j] == 0:
                matrix[i][0] = 0
                matrix[0][j] = 0
    
    # Use markers to set elements to zero
    for i in range(1, rows):
        for j in range(1, cols):
            if matrix[i][0] == 0 or matrix[0][j] == 0:
                matrix[i][j] = 0
    
    # Set first row and column to zero if needed
    if row_zero:
        for j in range(cols):
            matrix[0][j] = 0
    if col_zero:
        for i in range(rows):
            matrix[i][0] = 0
```

#### Input/Output

**Input:**
```
[
  [1, 1, 1],
  [1, 0, 1],
  [1, 1, 1]
]
```

**Output:**
```
[
  [1, 0, 1],
  [0, 0, 0],
  [1, 0, 1]
]
```

---

### 2. **Spiral Matrix**

Given an `m x n` matrix, return all elements of the matrix in spiral order.

#### Solution

```python
def spiral_order(matrix):
    res = []
    while matrix:
        # Take the first row
        res += matrix.pop(0)
        # Rotate the remaining matrix counterclockwise
        if matrix and matrix[0]:
            matrix = list(zip(*matrix))[::-1]
    return res
```

#### Input/Output

**Input:**
```
[
  [1, 2, 3],
  [4, 5, 6],
  [7, 8, 9]
]
```

**Output:**
```
[1, 2, 3, 6, 9, 8, 7, 4, 5]
```

---

### 3. **Rotate Image**

You are given an `n x n` 2D matrix representing an image. Rotate the image by 90 degrees (clockwise).

#### Solution

```python
def rotate(matrix):
    n = len(matrix)
    # Transpose the matrix
    for i in range(n):
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    
    # Reverse each row
    for i in range(n):
        matrix[i].reverse()
```

#### Input/Output

**Input:**
```
[
  [1, 2, 3],
  [4, 5, 6],
  [7, 8, 9]
]
```

**Output:**
```
[
  [7, 4, 1],
  [8, 5, 2],
  [9, 6, 3]
]
```

---

### 4. **Word Search**

Given a 2D board and a word, find if the word exists in the grid. The word can be constructed from letters of sequentially adjacent cells.

#### Solution

```python
def word_search(board, word):
    def dfs(i, j, k):
        if k == len(word):
            return True
        if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]) or board[i][j] != word[k]:
            return False
        
        tmp = board[i][j]
        board[i][j] = "#"
        
        found = (dfs(i+1, j, k+1) or
                 dfs(i-1, j, k+1) or
                 dfs(i, j+1, k+1) or
                 dfs(i, j-1, k+1))
        
        board[i][j] = tmp
        return found

    for i in range(len(board)):
        for j in range(len(board[0])):
            if dfs(i, j, 0):
                return True
    return False
```

#### Input/Output

**Input:**
```
board = [
  ['A', 'B', 'C', 'E'],
  ['S', 'F', 'C', 'S'],
  ['A', 'D', 'E', 'E']
]
word = "ABCCED"
```

**Output:**
```
True
```

---

These solutions handle various matrix-related problems with explanations for each approach.