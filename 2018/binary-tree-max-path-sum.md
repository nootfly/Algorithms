# Binary Tree Maximum Path Sum

Given a non-empty binary tree, find the maximum path sum.

For this problem, a path is defined as any sequence of nodes from some starting node to any node in the tree along the parent-child connections. The path must contain at least one node and does not need to go through the root.

## Code

```python
def max_path_sum(root):
    if root is None:
        return 0
    l = max(0, max_path_sum(root.left))
    r = max(0, max_path_sum(root.right))
    max_single = max(r, l) + root.val
    max_path_sum.ret = max(r + l + root.val, max_path_sum.ret)
    return max_single

def calc_max_path_sum(root):
    max_path_sum.ret = float('-inf')
    max_path_sum(root)
    return max_path_sum.ret
```

## Reference

[124. Binary Tree Maximum Path Sum](https://leetcode.com/problems/binary-tree-maximum-path-sum/description/)