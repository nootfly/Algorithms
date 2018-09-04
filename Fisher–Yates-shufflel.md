# Fisher–Yates shuffle

The Fisher-Yates shuffle is an algorithm for shuffling a sequence.

## Time Complexity

O(n)

## Solution

>The idea is to start from the last element, swap it with a randomly selected element from the whole array (including last). Now consider the array from 0 to n-2 (size reduced by 1), and repeat the process till we hit the first element.

## Code

```python
import random
def shuffle(arr):
    n = len(arr)
    for i in range(n - 1, 0, -1):
        j = random.randint(0, i)
        arr[i], arr[j] = arr[j], arr[i]
    return arr
```

## Reference

[Fisher–Yates shuffle](https://en.wikipedia.org/wiki/Fisher%E2%80%93Yates_shuffle)

[Shuffle a given array](https://www.geeksforgeeks.org/shuffle-a-given-array/)