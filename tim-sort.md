# Timsort

Timsort is a hybrid stable sorting algorithm, derived from merge sort and insertion sort, designed to perform well on many kinds of real-world data. 
Timsort has been Python's standard sorting algorithm since version 2.3. It is also used to sort arrays of non-primitive type in Java SE 7, on the Android platform,and in GNU Octave.

## Time Complexity

Timsort’s big O notation is O(n log n).

## Operation

Timsort was designed to take advantage of runs of consecutive ordered elements that already exist in most real-world data, natural runs. It iterates over the data collecting elements into runs, and simultaneously merging those runs together. When there are runs, doing this decreases the total number of comparisons needed to fully sort the list.

We divides the Array into blocks known as Run. We sort those runs using insertion sort one by one and then merge those runs using combine function used in merge sort. If size of Array is less than run, then Array get sorted just by using Insertion Sort. The size of run may vary from 32 to 64 depending upon size of array. Note that merge function performs well when sizes subarrays are powers of 2. The idea is based on the fact that insertion sort performs well for small arrays.

## References

[https://en.wikipedia.org/wiki/Timsort](https://en.wikipedia.org/wiki/Timsort)

[Timsort — the fastest sorting algorithm you’ve never heard of](https://hackernoon.com/timsort-the-fastest-sorting-algorithm-youve-never-heard-of-36b28417f399)

[TimSort](https://www.geeksforgeeks.org/timsort/)