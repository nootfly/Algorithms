# Sudoku

Sudoku is a puzzle where you're given a partially-filled 9 by 9 grid with digits. The objective is to fill the grid with the constraint that every row, column, and box (3 by 3 subgrid) must contain all of the digits from 1 to 9.

## Code

```python
def get_end(y):
    if 0 <= y <= 2:
        return 3
    elif 3 <= y <= 5:
        return 6
    else:
        return 9

def is_valid(mat, pos, num):
    x, y = pos[0], pos[1]
    for i in range(9):
        if mat[i][y] == num:
            return False
        if mat[x][i] == num:
            return False
    x_end = get_end(x)
    y_end = get_end(y)
    for i in range(x_end - 3, x_end):
        for j in range(y_end - 2, y_end):
            if mat[i][j] == num:
                return False
    return True

def fill_position(mat, spaces, n):
    if n == len(spaces):
        print(mat)
        return
    pos = spaces[n]

    for i in range(1, 10):
        if is_valid(mat, pos, i):
            mat[pos[0]][pos[1]] = i
            fill_position(mat, spaces, n + 1)
            mat[pos[0]][pos[1]] = -1

def sudoko(mat):
    spaces = []
    for i in range(9):
        for j in range(9):
            if mat[i][j] == - 1:
                spaces.append((i, j))

    fill_position(mat, spaces, 0)
```