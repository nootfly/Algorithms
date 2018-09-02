# Bottom-up Merge Sort

In recursive approach, the problem is broken down into smaller, simple subproblems in top-down manner until the solution becomes trivial.

## Code

```python
def merge(arr, tem, l, mid, h):
    k, i, j = l, l, mid + 1
    while i <= mid and j <=h:
        if arr[i] < arr[j]:
            tem[k] = arr[i]
            i += 1
        else:
            tem[k] = arr[j]
            j += 1
        k += 1
    while i <= mid:
       tem[k] = arr[i]
       k += 1
       i += 1
    for n in range(l, h + 1):
        arr[n] = tem[n]
        
def merge_sort(arr):
    low = 0
    high = len(arr) - 1
    tem = arr[:]
    m = 1
    # for m = 1, i = 0, 2, 4, 6, 8...
    # for m = 2, i = 0, 4, 8, 12...
    # for m = 4, i = 0, 8, 16...
    while m < high - low:
      i = low
      while i < high:
        l = i
        mid = i + m - 1
        to = min(i + 2 * m - 1, high)
        merge(arr, tem, l, mid, to)
        i += 2 * m
      m = 2 * m
```