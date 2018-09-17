# 4 Sum Problem

Given an unsorted array of integers, check if it contains four elements tuple (Quadruplets) having given sum.

## Solution

```swift
// four sum - swift
func fourSum(arr: [Int], sum: Int) -> Set<Set<Int>> {
    var dict:[Int:[(Int, Int)]] = [:]
    var result : Set = Set<Set<Int>>()
    for i in 0..<arr.count {
        for j in (i + 1)..<arr.count {
            if let pairs = dict[sum - (arr[i] + arr[j])] {
                for pair in pairs {
                    if (pair.0 != i && pair.1 != j) && (pair.0 != j && pair.1 != i) {
                        result.insert([arr[i], arr[j], arr[pair.0], arr[pair.1]])
                    }
                }
            }
            if var pairs = dict[arr[i] + arr[j]] {
                pairs.append((i, j))
            } else {
                dict[arr[i] + arr[j]] = [(i, j)]
            }
        }
    }
    return result
}
```

## References

[4 sum problem](http://www.techiedelight.com/4-sum-problem/)