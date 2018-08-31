# Reverse a linked List

Input:  1 -> 2 -> 3 -> 4 -> 5 -> 6 -> null, Output: 6 -> 5 -> 4 -> 3 -> 2 -> 1 -> null

## Code

```python
class Node(object):
      def __init__(self, val, next = None):
          self.val = val  
          self.next = next
        
class LinkedList(object):
      def __init__(self, head = None):
          self.head = head
                
      def reverse(self):
         curr = self.head
         pre = None   
         while curr:
              next = curr.next
              curr.next = pre
              pre = curr
              curr = next
                
         self.head = pre
```