# Uniform distribution

* [Uniform distribution](https://en.wikipedia.org/wiki/Uniform_distribution_(continuous))

  > A discrete uniform probability distribution is one in which all elementary events in the sample space have an equal opportunity of occurring. As a result, for a finite sample space of size n, the probability of an elementary event occurring is 1/n.
 
* [Reservoir Sampling](https://www.geeksforgeeks.org/reservoir-sampling/)

  > Reservoir sampling is a family of randomized algorithms for randomly choosing k samples from a list of n items, where n is either a very large or unknown number. Typically n is large enough that the list doesn’t fit into main memory. For example, a list of search queries in Google and Facebook.

  > So we are given a big array (or stream) of numbers (to simplify), and we need to write an efficient function to randomly select k numbers where 1 <= k <= n. Let the input array be stream[].
  
  [Select a random number from stream, with O(1) space and O(n) time](https://www.geeksforgeeks.org/select-a-random-number-from-stream-with-o1-space/) 

* [Segment Tree](https://www.geeksforgeeks.org/segment-tree-set-1-sum-of-given-range/)

  Representation of Segment trees
  1. Leaf Nodes are the elements of the input array.
  2. Each internal node represents some merging of the leaf nodes. The merging may be different for different problems. For this problem, merging is sum of leaves under a node.

  An array representation of tree is used to represent Segment Trees. For each node at index i, the left child is at index 2*i+1, right child at 2*i+2 and the parent is at (i - 1)/2

* [Binary Indexed Tree or Fenwick Tree](https://www.geeksforgeeks.org/binary-indexed-tree-or-fenwick-tree-2/)

   When compared with a flat array of numbers, the Fenwick tree achieves a much better balance between two operations: element update and prefix sum calculation.