# Two Prime Sum

Given an even number (greater than 2), return two prime numbers whose sum will be equal to the given number.
A solution will always exist. See [Goldbach’s conjecture](https://en.wikipedia.org/wiki/Goldbach%27s_conjecture).

## Solution

The idea is to find all the primes less than or equal to the given number N using Sieve of Eratosthenes. Once we have an array that tells all primes, we can traverse through this array to find pair with given sum.

## Code

```python
def all_primes(lst, n):
    lst[0] = lst[1] = False
    p = 2

    while p * p <= n:
      if lst[p] == True:
        i = 2 * p
        while i < n:
             lst[i] = False
             i += p

      p += 1
  
def two_prime(n):
    is_prime = [True] * (n + 1)
    all_primes(is_prime, n)
    for i in range(2, n):
       if is_prime[i] and is_prime[n - i]:
           return (i, n - i)
```

## Reference

[Find two prime numbers with given sum](https://www.geeksforgeeks.org/find-two-prime-numbers-with-given-sum/)