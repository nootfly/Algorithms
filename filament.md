# Filament

* [Filament - Google Android Open Source 2D and 3D Engine](https://google.github.io/filament/Filament.md.html)

  > Filament is a physically based rendering (PBR) engine for Android. The goal of Filament is to offer a set of tools and APIs for Android developers that will enable them to create high quality 2D and 3D rendering with ease.

* [How Numba and Cython speed up Python code](https://rushter.com/blog/numba-cython-python-optimization/)

  >Numba is a just-in-time (JIT) compiler that translates Python code to native machine instructions both for CPU and GPU. The code can be compiled at import time, runtime, or ahead of time.

* [Paint house question](http://tiancao.me/Leetcode-Unlocked/LeetCode%20Locked/c1.15.html)

  A builder is looking to build a row of N houses that can be of K different colors. He has a goal of minimizing cost while ensuring that no two neighboring houses are of the same color.

  Given an N by K matrix where the nth row and kth column represents the cost to build the nth house with kth color, return the minimum cost which achieves this goal.

  ```python
   import sys

   def min_cost(costs):
       n = len(costs)
       if n == 0:
           return
       k = len(costs[0])
       dp = [0] * k
       min1 = 0
       min2 = 0
       for i in range(n):
         premin1 = min1 if i > 0 else 0
         premin2 = min2 if i > 0 else 0
         min1 = sys.maxint
         min2 = sys.maxint
         for j in range(k):
           if dp[j] != premin1 or premin1 == premin2:
              dp[j] = premin1 + costs[i][j]
           else:
              dp[j] = premin2 + costs[i][j]
           if min1 <= dp[j]:
              min2 = min(min2, dp[j])
           else:
              min2 = min1
              min1 = dp[j]
       return min1
 ```   
