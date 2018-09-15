# Wiggle Sort

Given an unsorted array `nums`, reorder it such that `nums[0] < nums[1] > nums[2] < nums[3]...`

## Solution

```python
def wiggleSort(nums):
    n = len(nums)
    if nums is None or n == 0:
        return
    pre = nums[0]
    inc = True
    for i in range(1, n):
     if (inc and pre <= nums[i]) or (inc == False and pre >=nums[i]):
         nums[i - 1] = pre
         pre = nums[i]
     else:
         nums[i - 1] = nums[i]
     inc = not inc
    nums[n - 1] = pre
```

## References

[324. Wiggle Sort II](https://leetcode.com/problems/wiggle-sort-ii/description/)

[Google Interview - Wiggle Sort](http://yuanhsh.iteye.com/blog/2206429)
