# Find longest substring with k unique characters in a given string

For example : Given a string, find the longest substring which contains 2 unique characters. `"abcbbbbcccbdddadacb" => "bcbbbbcccb"`

## Solution

The problem can be solved in `O(n)`. Idea is to maintain a window and add elements to the window till it contains less or equal k, update our result if required while doing so. If unique elements exceeds than required in window, start removing the elements from left side.

## Code

```python
def find_longest_sub(string, k):
    if k == 0 or len(string) == 0 or k > len(string):
        return None
    dict = {}
    start = 0
    max_len = 0
    max_len_start = 0
    for i in range(len(string)):
        if string[i] in dict:
            dict[string[i]] += 1
        else:
            dict[string[i]] = 1
        while len(dict) > k:
            if dict[string[start]] == 1:
                del dict[string[start]]
            else:
                dict[string[start]] -= 1
            start += 1
        if i - start + 1 > max_len and len(dict) == k:
            max_len = i - start + 1
            max_len_start = start
    return string[max_len_start: max_len_start + max_len]
```

## References

[Longest Substring with At Most K Distinct Characters](https://www.programcreek.com/2013/02/longest-substring-which-contains-2-unique-characters/)

[Find the longest substring with k unique characters in a given string](https://www.geeksforgeeks.org/find-the-longest-substring-with-k-unique-characters-in-a-given-string/)