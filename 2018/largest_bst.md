# Largest BST in a Binary Tree

Given a Binary Tree, write a function that returns the size of the largest subtree which is also a Binary Search Tree (BST). If the complete Binary Tree is BST, then return the size of whole tree.

A Tree is BST if following is true for every node x.

1. The largest value in left subtree (of x) is smaller than value of x.
2. The smallest value in right subtree (of x) is greater than value of x.

## Code

```python
class Info:
      def __init__(self, size=0, max_val=None, min_val=None, answer=None, is_bst=False):
         self.size = size
         self.max_val = max_val
         self.min_val = min_val
         self.answer = answer
         self.is_bst = is_bst
      def __str__(self):
         return "answer is {}, max={}, min={}".format(self.answer, self.max_val, self.min_val)
def find_largest_bst(root):
    if root is None:
        return Info(0, -sys.maxsize + 1, sys.maxsize, 0, True)
    if root.left is None and root.right is None:
        return Info(1, root.val, root.val, 1, True)

    l_info = find_largest_bst2(root.left)
    r_info = find_largest_bst2(root.right)
    ret = Info()

    if l_info.is_bst and r_info.is_bst and l_info.max_val < root.val and r_info.min_val > root.val:
       ret.size = l_info.size + r_info.size + 1
       ret.max_val = max(r_info.max_val, max(l_info.max_val, root.val))
       ret.min_val = min(l_info.min_val, min(r_info.min_val, root.val))
       ret.answer = ret.size
       ret.is_bst = True
       return ret 
    
    ret.answer = max(l_info.answer, r_info.answer)
    ret.is_bst = False
    return ret
```

## References

[Largest BST in a Binary Tree | Set 2](https://www.geeksforgeeks.org/largest-bst-binary-tree-set-2/)

[Find the largest BST subtree in a given Binary Tree](https://www.geeksforgeeks.org/find-the-largest-subtree-in-a-tree-that-is-also-a-bst/)
