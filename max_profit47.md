# Daily Coding Problem 47

## Question

Given a array of numbers representing the stock prices of a company in chronological order, write a function that calculates the maximum profit you could have made from buying and selling that stock once. You must buy before you can sell it.

For example, given [9, 11, 8, 5, 7, 10], you should return 5, since you could buy the stock at 5 dollars and sell it at 10 dollars.

## Code

```python
def max_profit(prices):
    max_future_price, max_profit = 0, 0
    for index in range(len(prices) - 1, 0, -1):
        max_future_price = max(max_future_price, prices[index])
        max_profit = max(max_profit, max_future_price - prices[index - 1])
    return max_profit
```

## Reference

[daily_coding_problem_46_49.py](https://github.com/r1cc4rdo/daily_coding_problem/blob/master/daily_coding_problem_46_49.py)

[Daily Coding Problem](https://www.dailycodingproblem.com/)