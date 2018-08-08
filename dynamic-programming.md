# Dynamic Programming

>**Dynamic programming** is a method for solving a complex problem by breaking it down into a collection of simpler subproblems, solving each of those subproblems just once, and storing their solutions using a memory-based data structure (array, map,etc). This technique of storing solutions to subproblems instead of recomputing them is called memoization.

>Every Dynamic Programming problem has a schema to be followed:
>* Show that the problem can be broken down into *optimal sub-problems.
>* Recursively define the value of the solution by expressing it in terms of optimal solutions for smaller sub-problems.
>* Compute the value of the optimal solution in bottom-up fashion.
>* Construct an optimal solution from the computed information.

>Dynamic programming takes account of this fact and solves each sub-problem only once. This can be achieved in either of two ways –

>**Top-down approach (Memoization)**: This is the direct fall-out of the recursive formulation of any problem. If the solution to any problem can be formulated recursively using the solution to its sub-problems, and if its sub-problems are overlapping, then one can easily memoize or store the solutions to the sub-problems in a table. Whenever we attempt to solve a new sub-problem, we first check the table to see if it is already solved. If the sub-problem is already solved, we can use it’s solution directly, otherwise we solve the sub-problem and add its solution to the table.
 
>**Bottom-up approach (Tabulation)** Once we formulate the solution to a problem recursively as in terms of its sub-problems, we can try reformulating the problem in a bottom-up fashion: try solving the sub-problems first and use their solutions to build-on and arrive at solutions to bigger sub-problems. This is also usually done in a tabular form by iteratively generating solutions to bigger and bigger sub-problems by using the solutions to small sub-problems. For example, if we already know the values of F(i – 1) and F(i – 2), we can directly calculate the value of F(i).

The longest common subsequence (LCS) problem is the problem of finding the longest subsequence that is present in given two sequences in the same order. LCS length can be solved by Dynamic progrmaming.

  ```python
  def lcs_length(x, y, m, n, lookup):
    if m == 0 or n == 0:
       return 0
    key = str(m) + "|" + str(n)
    
    if key not in lookup:
       if x[m - 1] == y[n - 1]:
          lookup[key] = lcs_length(x, y, m - 1, n - 1, lookup) + 1
       else:
          lookup[key] = max(lcs_length(x, y, m - 1, n, lookup), lcs_length(x, y, m, n - 1, lookup))
    
    return lookup[key]
   ``` 

Reference:

[Introduction to Dynamic Programming](http://www.techiedelight.com/introduction-dynamic-programming/)

[Introduction to Dynamic Programming 1](https://www.hackerearth.com/zh/practice/algorithms/dynamic-programming/introduction-to-dynamic-programming-1/tutorial/)