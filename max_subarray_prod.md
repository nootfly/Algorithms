# Find maximum product subarray in a given array

Given an array of integers, find maximum product subarray. In other words, find a sub-array that has maximum product of its elements.

For example,

Input:  { -6, 4, -5, 8, -10, 0, 8 }

Output: The maximum product sub-array is {4, -5, 8, -10} having product 1600

## Code

```python
def find_max_product(arr):
    min_ending, max_ending, max_prod = 0, 0, 0
    for v in arr:
        temp = max_ending
        max_ending = max(v, max(v * max_ending, v * min_ending))
        min_ending = min(v, min(v * temp, v * min_ending))
        max_prod = max(max_prod, max_ending)
    return max_prod
```

```python
def find_max_product(arr):
    p, m, r = 0, 0, 0
    if len(arr) == 1:
        return arr[0]
    else:
       for v in arr:
         p = max(1, p) * v
         m *= v
         if p < 0:
           p, m = m, p
         r = max(p, r)
    return r
```

## References

[How do I solve maximum product subarray problems?](https://www.quora.com/How-do-I-solve-maximum-product-subarray-problems)

[Find maximum product subarray in a given array](http://www.techiedelight.com/find-maximum-product-subarray-given-array/)