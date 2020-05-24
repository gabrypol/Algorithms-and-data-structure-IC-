'''
Writing programming interview questions hasn't made me rich yet ... so I might give up and start trading Apple stocks all day instead.

First, I wanna know how much money I could have made yesterday if I'd been trading Apple stocks all day.

So I grabbed Apple's stock prices from yesterday and put them in a list called stock_prices, where:

The indices are the time (in minutes) past trade opening time, which was 9:30am local time.
The values are the price (in US dollars) of one share of Apple stock at that time.
So if the stock cost $500 at 10:30am, that means stock_prices[60] = 500.

Write an efficient function that takes stock_prices and returns the best profit I could have made from one purchase and one sale of one share of Apple stock yesterday.

For example:

  stock_prices = [10, 7, 5, 8, 11, 9]

get_max_profit(stock_prices)
# Returns 6 (buying for $5 and selling for $11)

No "shorting"—you need to buy before you can sell. Also, you can't buy and sell in the same time step—at least 1 minute has to pass.
'''

'''
Solution 1: brute force. I can iterate through stock_prices, and nest another loop to calculate the maximum profit. While doing that, I keep track of the maximum profit so far (buying first and selling afterwards, since shorting the stock is not allowed).
  Time: O(n^2)
  Space: (1)

def get_max_profit(stock_prices):
  if len(stock_prices) < 2:
    raise ValueError('The price list has less than two elements')

  max_profit_so_far = -math.inf
  for i in range(len(stock_prices)):
    for j in range(i + 1, len(stock_prices)):
      if stock_prices[j] - stock_prices[i] > max_profit_so_far:
        max_profit_so_far = stock_prices[j] - stock_prices[i]
  return max_profit_so_far
'''

# Solution 2:
import math

def get_max_profit(stock_prices):
  if len(stock_prices) < 2:
    raise ValueError('The price list has less than two elements')

  for i in range(1, len(stock_prices)):
    stock_prices[i - 1] = stock_prices[i] - stock_prices[i - 1]
  stock_prices[-1] = 0

  if max(stock_prices) <= 0:
    return max(stock_prices[:-1])
  else:
    sum_of_positive = 0
    for i, num in enumerate(stock_prices):
      if num > 0:
        sum_of_positive += num
    return sum_of_positive


prices = [9, 7, 4, 1]
print(get_max_profit(prices))

'''
Solution 2:
  Time: O(n)
  Space: (1)
'''