# Array Rotation Algorithm

Write a function rotate(arr[], d, n) that rotates arr[] of size n by d elements.

* Reverse Algorithm - Time Complexity : O(n)
  
  >Let AB are the two parts of the input array where A = arr[0..d-1] and B = arr[d..n-1]. The idea of the algorithm is :

  >* Reverse A to get ArB, where Ar is reverse of A.
  >* Reverse B to get ArBr, where Br is reverse of B.
  >* Reverse all to get (ArBr) r = BA.
  

  ```python
  def rotate_arr_reverse(arr, d, n):
    reverse(arr, 0, d - 1)
    reverse(arr, d, n - 1)
    reverse(arr, 0, n - 1)
  ```

* Juggling Algorithm

  >divide the array in different sets
where number of sets is equal to GCD of n and d and move the elements within sets.
If GCD is 1, then elements will be moved within one set only, we just start with temp = arr[0] and keep moving arr[i+d] to arr[i] and finally store temp at the right place.

  ```python
  def rotate_arr(arr, d, n):
    common = gcd(n, d)
    
    for i in range(common):
        temp = arr[i]
        start = i
        while 1:
            end = start + d
            if end >= n:
                end = end - n
            if end == i:
                break
            arr[start] = arr[end]
            start = end
                            
        arr[start] = temp
  ```        

* Block swap algorithm
  
  >Initialize A = arr[0..d-1] and B = arr[d..n-1]
  >1. Do following until size of A is equal to size of B

  >a) If A is shorter, divide B into Bl and Br such that Br is of same length as A. Swap A and Br to change ABlBr into BrBlA. Now A is at its final place, so recur on pieces of B.  

  >b)  If A is longer, divide A into Al and Ar such that Al is of same length as B Swap Al and B to change AlArB into BArAl. Now B is at its final place, so recur on pieces of A.

  >2. Finally when A and B are of equal size, block swap them.

  ```python
  def left_rotate(arr, d, n):
    #print "arr = %s, d=%d, n=%d" % (str(arr), d, n)
    if d == 0 or d == n:
        return
    if n - d == d: 
       swap(arr, 0, n - d, d)
       #print arr
       return

    if d < n - d:
        swap(arr, 0, n - d, d)
        left_rotate(arr, d, n - d)
    else:
        swap(arr, 0, d, n - d)
        left_rotate(arr[n - d:], 2 * d - n , d)
```