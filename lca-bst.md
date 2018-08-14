# Find Lowest Common Ancestor (LCA) in a Binary Tree

Given a binary tree and two nodes x and y in it, find lowest common ancestor (LCA) of x and y in it.

>We can recursively find lowest common ancestor of nodes x and y present in the binary tree. The trick is to find the node in binary tree which has one key present in its left subtree and the other key present in right subtree. If any such node is present in the tree, then it is LCA else if y lies in subtree rooted at node x, then x is the LCA else if x lies in subtree rooted at node y, then y is the LCA.


  ```python
   def lca_bst(root, x, y):
    
    if not root:
        return None
    
    big = max(x, y)
    small = min(x, y)
    if root.val > small and root.val < big:
        return root.val
    if root.val > small and root.val > big:
        return lca_bst(root.left, x, y)
    
    if root.val < small and root.val < big:
        return lca_bst(root.right, x, y)
    
    if root.val == small:
        return small
    
    if root.val == big:
        return big
  ```


References:

[Find Lowest Common Ancestor (LCA) of Two Nodes in a Binary Tree](http://www.techiedelight.com/find-lowest-common-ancestor-lca-two-nodes-binary-tree/)
