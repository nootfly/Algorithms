# Longest palindromic substring

Given a string, find maximum-length contiguous substring of it that is also a palindrome. For example, the longest palindromic substring of "bananas" is "anana" and longest palindromic substring of "abdcbcdbdcbbc" is "bdcbcdb".

## Solution


## Simple Solution

```python
def expand(string, l, h):
    while l >= 0 and h < len(string) and string[l] == string[h]:
         l -= 1
         h += 1
    return string[l + 1: h] 

def find_longest_parlindromic_substring(string):
    max_str = ''
    max_len = 0
    for i in range(len(string)):
        curr_str = expand(string, i, i)
        curr_len = len(curr_str)
        if curr_len > max_len:
            max_str = curr_str
            max_len = curr_len
  
        curr_str = expand(string, i, i + 1)
        curr_len = len(curr_str)
        if curr_len > max_len:
            max_str = curr_str
            max_len = curr_len
    return max_str
```

## Manacher algorithm

```python
class Solution:
    #Manacher algorithm
    #http://en.wikipedia.org/wiki/Longest_palindromic_substring
    
    def longestPalindrome(self, s):
        # Transform S into T.
        # For example, S = "abba", T = "^#a#b#b#a#$".
        # ^ and $ signs are sentinels appended to each end to avoid bounds checking
        T = '#'.join('^{}$'.format(s))
        n = len(T)
        P = [0] * n
        C = R = 0
        for i in range (1, n-1):
            P[i] = (R > i) and min(R - i, P[2*C - i]) # equals to i' = C - (i-C)
            # Attempt to expand palindrome centered at i
            while T[i + 1 + P[i]] == T[i - 1 - P[i]]:
                P[i] += 1
    
            # If palindrome centered at i expand past R,
            # adjust center based on expanded palindrome.
            if i + P[i] > R:
                C, R = i, i + P[i]
    
        # Find the maximum element in P.
        maxLen, centerIndex = max((n, i) for i, n in enumerate(P))
        return s[(centerIndex  - maxLen)//2: (centerIndex  + maxLen)//2]
```

## Reference

[Longest palindromic substring (Non-DP space optimized solution)](http://www.techiedelight.com/longest-palindromic-substring-non-dp-space-optimized-solution/)

[Longest Palindromic Substring O(N) Manacher's Algorithm](https://www.youtube.com/watch?v=nbTSfrEfo6M)

[Longest Palindromic Substring](https://leetcode.com/problems/longest-palindromic-substring/discuss/3337/manacher-algorithm-in-python-on)