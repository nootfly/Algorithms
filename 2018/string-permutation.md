# All permutations of a given string

A permutation, also called an "arrangement number" or "order" is a rearrangement of the elements of an ordered list S into a one-to-one correspondence with S itself. A string of length n has n! permutation.

Below are the permutations of string `ABC`.

Assume all characters are unique.

`ABC ACB BAC BCA CBA CAB`

## Backtracking Solution

```python
def permute(string, start = 0):
    length = len(string)
    if start == length - 1:
        print(''.join(string))
    else:
        for i in range(start, length):
            string[start], string[i] = string[i], string[start]
            permute(string, start + 1)
            string[start], string[i] = string[i], string[start] # backtrack
def permutation(string):
    permute(string)
```

## Recursive Algorithm

```python
def permutation(lst):
    if len(lst) == 0:
        return []
    if len(lst) == 1:
        return [lst]
    ret = []

    for i in range(len(lst)):
       m = lst[i]
       remLst = lst[:i] + lst[i+1:]
       for p in permutation4(remLst):
           ret.append(m + p)
    return ret
```

## Reference

[Write a program to print all permutations of a given string](https://www.geeksforgeeks.org/write-a-c-program-to-print-all-permutations-of-a-given-string/)

[Generate all permutation of a set in Python](https://www.geeksforgeeks.org/generate-all-the-permutation-of-a-list-in-python/)

[Finding all possible permutations of a given string in python](https://stackoverflow.com/questions/8306654/finding-all-possible-permutations-of-a-given-string-in-python)