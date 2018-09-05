# LRU

Implement an LRU (Least Recently Used) cache. It should be able to be initialized with a cache size n, and contain the following methods:

set(key, value): sets key to value. If there are already n items in the cache and we are adding a new item, then it should also remove the least recently used item.
get(key): gets the value at key. If no such key exists, return null.
Each operation should run in O(1) time.

## Code

```python
from collections import OrderedDict

class LRU:
      def __init__(self, capacity = 10):
          self._dict = OrderedDict()
          self._capacity = capacity 
            
      def get(self, key):
          if key not in self._dict:
              return None
          value = self._dict[key]
          del self._dict[key]
          self._dict[key] = value
          return value
            
    
      def set(self, key, value):
    
          if len(self._dict) + 1 > self._capacity:
              self._dict.popitem(last=False)
              
          if key not in self._dict:
             self._dict[key] = value   
          else:
              del self._dict[key]
              self._dict[key] = value
```

## References

[How to implement LRU cache using HashMap and Doubly Linked List](https://medium.com/@krishankantsinghal/my-first-blog-on-medium-583159139237)

[LRUCache.swift](https://github.com/raywenderlich/swift-algorithm-club/blob/master/LRU%20Cache/LRUCache.swift)