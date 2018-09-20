# Toss biased

Assume you have access to a function toss_biased() which returns 0 or 1 with a probability that's not 50-50 (but also not 0-100 or 100-0). You do not know the bias of the coin. Write a function to simulate an unbiased coin toss.

## Solution

The observation is that if you have a biased coin that comes up heads with probability p, and if you flip the coin twice, then:

The probability that it comes up heads twice is p * p
The probability that it comes up heads first and tails second is p(1-p)
The probability that it comes up tails first ands heads second is (1-p)p
The probability that it comes up tails twice is (1-p) * (1-p)

According to Bayes' theorem,  P(first coin is heads | both coins are different) = P(both coins are different | first coin is heads) P(first coin is heads) / P(both coins are different), P(first coin is heads | both coins are different) = p (1-p) / (2p(1-p)) = 1 / 2.

## Code

```python
def toss_unbiased():
    while true:
        v1 = toss_biased()
        v2 = toss_biased()
        if v1 != v2:
            return v1
```

## Reference

[Make a fair coin from a biased coin](https://stackoverflow.com/a/5429219)