# Counting Sort

Counting sort is an algorithm for sorting a collection of objects according to keys that are between a small range.

## Algorithm

The algorithm loops over the items, computing counts of times each key and insert value in an array. The index of the array is used as count keys. It then performs a prefix sum computation (a second loop, over the range of possible keys) to determine, for each key, the starting position in the output array of the items having that key. Finally, it loops over the items again, moving each item into its sorted position in the output array.

## Time Complexity

Time Complexity: O(n+k) where n is the number of elements in input array and k is the range of input. Auxiliary Space: O(n+k)

## Code

  ```python
   def counting_sort(arr):
    count = [0 for _ in range(10)]
    ret = [None for _ in range(len(arr))]
    
    for value in arr:
        count[value] += 1
     
    total = 0    
    for idx, value in enumerate(count):
        oldcount = count[idx]
        count[idx] = total
        total += oldcount
    
    for value in arr:
        ret[count[value]] = value
        count[value] += 1
    return ret
  ```

## References:

[https://en.wikipedia.org/wiki/Counting_sort](https://en.wikipedia.org/wiki/Counting_sort)

[Counting Sort](https://www.geeksforgeeks.org/counting-sort/)

[Learn Counting Sort Algorithm in LESS THAN 6 MINUTES!](https://www.youtube.com/watch?v=OKd534EWcdk)
