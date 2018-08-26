# Median-Finding Algorithm

Median finding algorithms (also called linear-time selection algorithms) use a divide and conquer strategy to efficiently compute the th smallest number in an unsorted list of size , where  is an integer between  and . Selection algorithms are often used as part of other algorithms, for example, they are used to help select a pivot in quicksort and used to determine th order statistics such as the maximum, minimum, and median elements in a list.

## Time Complexity

O(n)

## Example

### Question

find the fourth lowest element in `A = [25, 21, 98, 100, 76, 22, 43, 60, 89, 87]`

### Solution

First we break the list into lists of five elements.

`A1 =[25, 21, 98, 100, 76]` and `A2 = [22, 43, 60, 89, 87]`

Sort each list `A1` and `A2`

Then, get the medians out of each list and put them in a list of medians `M = [76, 60]`

sort this: `M = [60, 76]`

Pick the median from that list — since the length of the list is 2, and we determine the index of the median by the length of the list divided by two, we get: 2/2=1, the index of the median is 1 and `M[1] = 76`.

Use this as the pivot element and put all elements in  that are less than 76 to the left and all elements greater than 76 to the right.

`A' = [25, 22, 43, 60, 21, 76, 100, 89, 87, 98]`

Find the index of 76 which is 5. How 5 compare with 3? so we must recurse on the left half of the list  which is .

This list is only five elements long, so we can sort it and find what is at index 3.  and 43 is at index three, so it is the fourth smallest number of `A`.

## Code

```python
def median_of_medians(A, i):

    #divide A into sublists of len 5
    sublists = [A[j:j+5] for j in range(0, len(A), 5)]
    medians = [sorted(sublist)[len(sublist)/2] for sublist in sublists]
    if len(medians) <= 5:
        pivot = sorted(medians)[len(medians)/2]
    else:
        #the pivot is the median of the medians
        pivot = median_of_medians(medians, len(medians)/2)

    #partitioning step
    low = [j for j in A if j < pivot]
    high = [j for j in A if j > pivot]

    k = len(low)
    if i < k:
        return median_of_medians(low,i)
    elif i > k:
        return median_of_medians(high,i-k-1)
    else: #pivot = k
        return pivot
```

## Reference

[Median-Finding Algorithm](https://brilliant.org/wiki/median-finding-algorithm/)

[2. Divide & Conquer: Convex Hull, Median Finding](https://www.youtube.com/watch?v=EzeYI7p9MjU)

[My Favorite Algorithm: Linear Time Median Finding](https://rcoh.me/posts/linear-time-median-finding/)

[Selection algorithm](https://en.wikipedia.org/wiki/Selection_algorithm)