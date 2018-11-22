# Tower of Hanoi

The Tower of Hanoi is a puzzle game with three rods and n disks, each a different size.

Write a function that prints out all the steps necessary to complete the Tower of Hanoi. You should assume that the rods are numbered, with the first rod being 1, the second (auxiliary) rod being 2, and the last (goal) rod being 3.

For example, with n = 3, we can do this in 7 moves:

 Move 1 to 3,
 Move 1 to 2,
 Move 3 to 2,
 Move 1 to 3,
 Move 2 to 1,
 Move 2 to 3,
 Move 1 to 3,

## Code

 ```python
 def move_disk(start, empty, end, n):  
    if n == 0:
        return []
        
    ret = move_disk2(start, end, empty, n - 1)
    ret.append('Move {} to {}'.format(start, end))
    ret += move_disk2(empty, start, end, n - 1)
    return ret
                  
def hanoi_move(n):
    if n == 0:
        return
    ret = move_disk2(1, 2, 3, n)
    print(ret)
 ```

## Reference

 [Tower of Hanoi](http://interactivepython.org/runestone/static/pythonds/Recursion/TowerofHanoi.html)