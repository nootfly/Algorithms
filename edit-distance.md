# Edit distance

Edit distance may also be referred to as Levenshtein distance. The edit distance between two words is the minimum number of single-character edits (insertions, deletions or substitutions) required to change one word into the other. For example, the Levenshtein distance between "kitten" and "sitting" is 3.

## Solution

>Computing the Levenshtein distance is based on the observation that if we reserve a matrix to hold the Levenshtein distances between all prefixes of the first string and all prefixes of the second, then we can compute the values in the matrix in a dynamic programming fashion, and thus find the distance between the two full strings as the last value computed.

>It turns out that only two rows of the table are needed for the construction if one does not want to reconstruct the edited input strings (the previous row and the current row being calculated).

The Levenshtein distance may be calculated iteratively using the following algorithm:

   ```python
   def edit_distance(string1, string2):
    if len(string1) < len(string2):
        return edit_distance2(string2, string1)
    
    if len(string2) == 0:
        return len(string1)
    
    pre_line = range(len(string2) + 1)
    for i, c1 in enumerate(string1):
        curr_line = [i + 1]
        for j, c2 in enumerate(string2):
            insertions = pre_line[j + 1] + 1
            deletions = curr_line[j] + 1
            substitutions = pre_line[j] + (c1 != c2)
            curr_line.append(min(insertions, deletions, substitutions))
            
        pre_line = curr_line    
            
    return pre_line[-1] 
   ```

References:

[Algorithm Implementation/Strings/Levenshtein distance](https://en.wikibooks.org/wiki/Algorithm_Implementation/Strings/Levenshtein_distance#Python)

[Levenshtein distance](https://en.wikipedia.org/wiki/Levenshtein_distance)

[Minimum Edit Distance Dynamic Programming](https://www.youtube.com/watch?v=We3YDTzNXEk)