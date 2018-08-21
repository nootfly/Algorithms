# Boyer–Moore majority vote algorithm

Given an array of integers containing duplicates, return the majority element in an array if present. A majority element appears more than n/2 times where n is the size of the array.

## Algorithm

The algorithm maintains a counter variable and an element variable.  It then processes the elements of the sequence, one at a time. When processing an element x, if the counter is zero, the algorithm stores x as its the element variable. and sets the counter to one. Otherwise, it compares x to the stored element and either increments the counter (if they are equal) or decrements the counter (otherwise).

## Time Complexity

O(n)

## Code

  ```python
 def find_majority(arr):
    count, element = 0, None
    for i in range(len(arr)):
        if count == 0:
            element = arr[i]
            count = 1
        elif element == arr[i]:
             count += 1
        else:
            count -= 1        
    if count >= len(arr) // 2:
        return element
   ```

## References

[Find majority element in an array](http://www.techiedelight.com/find-majority-element-in-an-array-boyer-moore-majority-vote-algorithm/)