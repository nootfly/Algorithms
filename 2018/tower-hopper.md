# The Tower Hopper problem

The Tower Hopper problem gives us an array of values representing heights that express how far we can jump from a certain tower, and asks whether there's a way to get from tower[0] (0 indexed) to outside of the array.

For example, if we have towers = [4, 2, 0, 0, 2, 0], we can jump from towers[0] to towers[4] and then outside of the bounds of the array. Or we could jump from towers[0] to towers[1] to towers[4] and then out of the array. But if we had towers = [4, 2, 0, 0, 1, 0], there would be no way to hop out of the array and we should return False.

## Code

```python
def jump(towers, start, end):
    if start > end:
       return True
    if towers[start] > 0:
       i = 1
       while i <= towers[start]:
           if jump(towers, start + 1, end):
               return True
           i += 1
       return False
def is_hoppable(towers):
    return jump(towers, 0, len(towers) - 1)
```
