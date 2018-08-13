# 0-1 Knapsack problem

In 0-1 Knapsack problem, we are given a set of items, each with a weight and a value and we need to select items to maximize the total value while still keeping the total weight under or equal to a given limit.

## Time Complexity

The time complexity of Dynamic Programming solution is O(nW) where n is the number of items in the input and W is the Knapsack capacity. Auxiliary space used by the program is also O(nW).

## Dynamic programming

Top-down and bottom-up approaches can be used to solve this problem.

  ```python
  def knapsack_top_down(value_arr, weight_arr, n, capacity, cache):
    if capacity < 0:
        return -1
    if n < 0 or capacity == 0:
       return 0

    key = str(n) + '|' + str(capacity)
    
    if key in cache:
        return cache[key]
    
    result = 0
    if weight_arr[n] > capacity:
       result = knapsack_top_down(value_arr, weight_arr, n - 1, capacity, cache)
    else:
       temp1 = knapsack_top_down(value_arr, weight_arr, n - 1, capacity, cache)
       temp2 = value_arr[n] + knapsack_top_down(value_arr, weight_arr, n - 1, capacity - weight_arr[n], cache)
       result = max(temp1, temp2)
    cache[key] = result
    return result

def knapsack_bottom_up(value_arr, weight_arr, capacity):
    count = len(value_arr)
    
    lookup = [[0 for _ in range(capacity + 1)] for _ in range(count + 1)]
    
    for i in range(1, count + 1):
        for j in range(capacity + 1):
           if weight_arr[i - 1] > j:
                lookup[i][j] = lookup[i - 1][j]
           else:
                lookup[i][j] = max(lookup[i - 1][j], lookup[i - 1][j - weight_arr[i - 1]] + value_arr[i - 1])
                
    return lookup[count][capacity]
  ```



