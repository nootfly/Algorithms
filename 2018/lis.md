# Longest Increasing Subsequence

The Longest Increasing Subsequence (LIS) problem is to find the length of the longest subsequence of a given sequence such that all elements of the subsequence are sorted in increasing order. For example, the length of LIS for [10, 22, 9, 33, 21, 50, 41, 60, 80] is 6 and LIS is [10, 22, 33, 50, 60, 80]

## DP solution

```python
def find_longest_sub(arr):
    n = len(arr)
    lookup = [1] * n
    for i in range(1, n):
        for j in range(i):
            if arr[j] < arr[i] and lookup[j] + 1 > lookup[i]:
                lookup[i] = lookup[j] + 1
    return max(lookup)
```

## 

## Reference

[perm_identity
Longest Increasing Subsequence](https://www.geeksforgeeks.org/longest-increasing-subsequence-dp-3/)