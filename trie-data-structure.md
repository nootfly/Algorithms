# Trie

The word trie comes from retrieval. A trie (pronounced "try") is a tree-based data structure, which is used for efficient retrieval of a key in a large data-set of strings. Tries are also known as radix trees or prefix trees. Time complexity of a Trie data structure for insertion/deletion/search operation is just O(n) where n is key length.

* Store Characters in nodes (not keys)

* Each node has R children, one for each possible character.

Trie can be used for autocomplete, spell checker, and prefix matching.

  ```python
  class Trie(object):
      def __init__(self):
        self.isleaf = False
        self.children = {}
        
      def __str__(self):
          return "isleaf:" + str(self.isleaf) + " children=" + str(self.children)
        
      def insert(self, key):
          curr = self
          for char in key: 
             if char not in curr.children:
                 curr.children[char] = Trie()
             curr = curr.children[char]
            
          curr.isleaf = True  
      
      def search(self, key):
           curr = self 
           for char in key:
               if char in curr.children:
                 curr = curr.children[char]
               else:
                 return False
                            
           return curr.isleaf
    
       def delete(self, key):
           curr = self  
           for idx, char in enumerate(key):
               if char in curr.children:
                 curr = curr.children[char]
               else:
                 return False
                            
           return curr.isleaf 
  ```

Reference:

[Princeton Algorithms](https://algs4.cs.princeton.edu/lectures/52Tries.pdf)

[Implement Trie Data Structure in Java](http://www.techiedelight.com/implement-trie-data-structure-java/)
