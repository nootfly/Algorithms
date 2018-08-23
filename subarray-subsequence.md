# Print all subarrays and subsequences

For [1, 2, 3, 4, 5, 6], print all subarrays and subsequences

## Subarrays

  ```python
   def print_subarrays(arr):
       for i in range(len(arr)):
          for j in range(i, len(arr)):
            temp = []
            for k in range(i, j + 1):
                temp.append(arr[k])
            print(temp)    
  ```
result:
[1]
[1, 2]
[1, 2, 3]
[1, 2, 3, 4]
[1, 2, 3, 4, 5]
[1, 2, 3, 4, 5, 6]
[2]
[2, 3]
[2, 3, 4]
[2, 3, 4, 5]
[2, 3, 4, 5, 6]
[3]
[3, 4]
[3, 4, 5]
[3, 4, 5, 6]
[4]
[4, 5]
[4, 5, 6]
[5]
[5, 6]
[6]
## Subsequences

  ```python
   import math
   def print_subsequences(arr):
       all_bits = math.power(2, len(arr))
       for i in range(1, all_bits):
          temp = []
          for j in range(len(arr)):
            if (i & ( 1 << j)):
               temp.append(arr[j])
          print(temp)     
                
  ```  
Result: [1]
[2]
[1, 2]
[3]
[1, 3]
[2, 3]
[1, 2, 3]
[4]
[1, 4]
[2, 4]
[1, 2, 4]
[3, 4]
[1, 3, 4]
[2, 3, 4]
[1, 2, 3, 4]
[5]
[1, 5]
[2, 5]
[1, 2, 5]
[3, 5]
[1, 3, 5]
[2, 3, 5]
[1, 2, 3, 5]
[4, 5]
[1, 4, 5]
[2, 4, 5]
[1, 2, 4, 5]
[3, 4, 5]
[1, 3, 4, 5]
[2, 3, 4, 5]
[1, 2, 3, 4, 5]
[6]
[1, 6]
[2, 6]
[1, 2, 6]
[3, 6]
[1, 3, 6]
[2, 3, 6]
[1, 2, 3, 6]
[4, 6]
[1, 4, 6]
[2, 4, 6]
[1, 2, 4, 6]
[3, 4, 6]
[1, 3, 4, 6]
[2, 3, 4, 6]
[1, 2, 3, 4, 6]
[5, 6]
[1, 5, 6]
[2, 5, 6]
[1, 2, 5, 6]
[3, 5, 6]
[1, 3, 5, 6]
[2, 3, 5, 6]
[1, 2, 3, 5, 6]
[4, 5, 6]
[1, 4, 5, 6]
[2, 4, 5, 6]
[1, 2, 4, 5, 6]
[3, 4, 5, 6]
[1, 3, 4, 5, 6]
[2, 3, 4, 5, 6]
[1, 2, 3, 4, 5, 6]
