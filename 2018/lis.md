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

## NLOGN solution

```python
def ceil_index(arr, l, r, key):
    while r - l > 1:
        m = l + (r - l) // 2
        if arr[m] >= key:
            r = m
        else:
            l = m
    return r
def find_longest_sub(arr, size):
    print("tail_table")
    tail_table = [0 for i in range(size + 1)]
    tail_table[0] = arr[0]
    len = 1
    for i in range(1, size):
        if arr[i] < tail_table[0]:
            tail_table[0] = arr[i]
        elif arr[i] > tail_table[len - 1]:
            tail_table[len] = arr[i]
            len += 1
        else:
            tail_table[ceil_index(tail_table, -1, len - 1, arr[i])] = arr[i]
    return len
```

## Reference

[Longest Increasing Subsequence](https://www.geeksforgeeks.org/longest-increasing-subsequence-dp-3/)

[Longest Increasing Subsequence Size (N log N)](https://www.geeksforgeeks.org/longest-monotonically-increasing-subsequence-size-n-log-n/)

[longest increasing subsequence using dynamic programming?](https://stackoverflow.com/questions/2631726/how-to-determine-the-longest-increasing-subsequence-using-dynamic-programming)

[Longest increasing subsequence](http://www.cs.princeton.edu/courses/archive/spring13/cos423/lectures/LongestIncreasingSubsequence-2x2.pdf)