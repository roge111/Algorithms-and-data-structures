def maxProfit(prices):
    min_price = 10**4 + 1
    max_profit = 0

    for price in prices:
        if price < min_price:
            min_price = price
        elif price - min_price > max_profit:
            max_profit = price - min_price
    return max_profit

print(maxProfit([7,6,4,3,1]))