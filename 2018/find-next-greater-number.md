# Find next greater number with same set of digits

Given a number represented by a list of digits, find the next greater permutation of a number, in terms of lexicographic ordering. If there is not greater permutation possible, return the permutation with the lowest value/ordering.
For example, the list [1,2,3] should return [1,3,2]. The list [1,3,2] should return [2,1,3]. The list [3,2,1] should return [1,2,3].

## Algorithm

Following is the algorithm for finding the next greater number.

I) Traverse the given number from rightmost digit, keep traversing till you find a digit which is smaller than the previously traversed digit. For example, if the input number is "534976", we stop at 4 because 4 is smaller than next digit 9. If we do not find such a digit, then reverse the number.

II) Now search the right side of above found digit '4' for the smallest digit greater than '4'. For “534976″, the right side of 4 contains “976”. The smallest digit greater than 4 is 6.

III) Swap the above found two digits, we get 536974 in above example.

IV) Now sort all digits from position next to '4' to the end of number. The number that we get after sorting is the output. For above example, we sort digits in bold 536974. We get "536479" which is the next greater number for input 534976.

## Code

```python
def calc_next_permu(l):
    count = len(l)
    i = count
    if i < 2:
        return l
    while i - 2 >= 0 and l[i - 1] < l[i - 2]:
          i -= 1
    if i - 2 >= 0 and l[i - 1] > l[i - 2]:
       smallest = l[-1]
       smallest_idx = count - 1
       if count - 2 > i - 2: 
         for j in range(count - 2, i - 2, -1):
            if l[j] < smallest:
                smallest = l[j]
                smallest_idx = j
       l[i - 2], l[smallest_idx] = l[smallest_idx], l[i - 2]
       l[i - 1:] = sorted(l[i - 1:])
    if i == 1:
       l.reverse()
```

## References

[Find next greater number with same set of digits](https://www.geeksforgeeks.org/find-next-greater-number-set-digits/)