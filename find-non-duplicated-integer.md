# Find and return the no-duplicated integer

## Question

Given an array of integers where every integer occurs three times except for one integer, which only occurs once, find and return the non-duplicated integer.

For example, given [6, 1, 3, 3, 3, 6, 6], return 1. Given [13, 19, 13, 13], return 19.

Do this in O(N) time and O(1) space.

## Solution

```python
def find_unique(arr):
    ones = 0
    twos = 0
    for value in arr:
       twos |= (ones & value)
       ones ^= value
       not_threes = ~(ones & twos)
       ones &= not_threes
       twos &= not_threes

    return ones

```

## Reference

[Find the element that appears once](https://www.geeksforgeeks.org/find-the-element-that-appears-once/)