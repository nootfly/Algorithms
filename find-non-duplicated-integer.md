# Find and return the no-duplicated integer

## Question

Given an array of integers where every integer occurs three times except for one integer, which only occurs once, find and return the non-duplicated integer.

For example, given [6, 1, 3, 3, 3, 6, 6], return 1. Given [13, 19, 13, 13], return 19.

Do this in O(N) time and O(1) space.

## Solution

Basically, it makes use of the fact that x^x = 0. So all paired elements get XOR'd and vanish leaving the lonely element.  
ones - At any point of time, this variable holds XOR of all the elements which have 
appeared "only" once. 
twos - At any point of time, this variable holds XOR of all the elements which have 
appeared "only" twice. 
1. A new number appears - It gets XOR'd to the variable "ones". 
2. A number gets repeated(appears twice) - It is removed from "ones" and XOR'd to the 
variable "twice". 
3. A number appears for the third time - It gets removed from both "ones" and "twice". 


## Code

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

[Google Interview Question for Software Engineer / Developers](https://www.careercup.com/question?id=7902674)

[Find the element that appears once](https://www.geeksforgeeks.org/find-the-element-that-appears-once/)