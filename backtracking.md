# Backtracking

> Backtracking is an effective technique for solving algorithmic problems. In backtracking, we search depth-first for solutions, backtracking to the last valid path as soon as we hit a dead end.
> 
> Backtracking reduces the search space since we no longer have to follow down any paths we know are invalid. This is called pruning.
>  
> Backtracking is an effective technique for solving algorithmic problems. In backtracking, we search depth-first for solutions, backtracking to the last valid path as soon as we hit a dead end.

>Backtracking reduces the search space since we no longer have to follow down any paths we know are invalid. This is called pruning. We must be able to test partial solutions: for example, we can't find a global optimum using backtracking, since we have no idea if the solution we're currently on can lead to it or not. But we can, for example, solve Sudoku using backtracking. We can know immediately if our solution so far is invalid by testing if two of the same number appear in the same row, column, or square.

>While backtracking is useful for hard problems to which we do not know more efficient solutions, it is a poor solution for the everyday problems that other techniques are much better at solving.

>However, dynamic programming and greedy algorithms can be thought of as optimizations to backtracking, so the general technique behind backtracking is useful for understanding these more advanced concepts. 

[Eight queens puzzle](https://en.wikipedia.org/wiki/Eight_queens_puzzle) can be solved by backtracking

 ```python
   def n_queens(n, board=[]):
     if n == len(board):
         return 1
 
     count = 0
     for col in range(n):
         board.append(col)
         if is_valid(board):
             count += n_queens(n, board)
         board.pop()
     return count
  
   def is_valid(board):
     current_queen_row, current_queen_col = len(board) - 1, board[-1]
     # Check if any queens can attack the last queen.
     for row, col in enumerate(board[:-1]):
         diff = abs(current_queen_col - col)
         if diff == 0 or diff == current_queen_row - row:
             return False
     return True
 ```     

 Reference:

 [Backtracking](https://en.wikipedia.org/wiki/Backtracking)

 [Algorithms/Backtracking](https://en.wikibooks.org/wiki/Algorithms/Backtracking)
