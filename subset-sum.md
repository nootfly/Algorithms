# Subset Sum Problem

Given a set of positive integers and an integer s, is there any non-empty subset whose sum to s.

## Solution

As this problem has `optimal substructure` and `overlapping subproblems`, it can be solved using `Dynamic Programming`

## Time Complexity

O(n x sum)

## Top down approach

```python
def subset_sum(arr, k, n, cache):
    if k == 0:
        return True
    if n < 0 or k < 0:
        return False
    
    key = str(n) + '|' + str(k)
    if key in cache:
        return cache[key]
    
    cache[key] = subset_sum(arr, k, n - 1, cache) or subset_sum(arr, k - arr[n], n - 1, cache)
    return cache[key]
```

## Bottom up approach

```python
def subset_sum(arr, k):
    lookup = [[False for _ in range(len(arr) + 1)] for _ in range(k + 1)]
    
    for i in range(len(arr) + 1):
        lookup[0][i] = True
        
    for j in range(1, k + 1):
        lookup[j][0] = False
    
    for i in range(k + 1):
        for j in range(1, len(arr) + 1):
          lookup[i][j] = lookup[i][j - 1]
          if i >= arr[j - 1]:
               lookup[i][j] = lookup[i][j] or lookup[i - arr[j - 1]][j - 1] 

    return lookup[k][len(arr)]
```

## Get a subset

```python
def get_sebset_sum(arr, k):
    if k == 0:
        return []
    
    valid_nums = [value for value in arr if 0 < value <= k]
    for num in sorted(valid_nums, reverse=True):
       other_nums = valid_nums[:]
       other_nums.remove(num)
       ret =  get_sebset_sum(other_nums, k - num)
       if ret != None:
            return [num] + ret
    return None  
```

## Reference

[Subset Sum Problem](http://www.techiedelight.com/subset-sum-problem/)

[daily_coding_problem_41_45.py](https://github.com/r1cc4rdo/daily_coding_problem/blob/master/daily_coding_problem_41_45.py)
