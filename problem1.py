def myprofit(prices_list):
    minprice = prices_list[0]

    maxprofit = 0

    for price in prices_list:
        minprice = min(minprice, price)
        profit = price - minprice
        maxprofit = max(maxprofit, profit)

    return maxprofit


def mymargin(prices_day):

    max_margin = 0

    for i in range(len(prices_day) - 1):
        price_diff = abs(prices_day[i] - prices_day[i+1])
        max_margin = max(max_margin, price_diff)

    return max_margin


myprofit([10, 23, 22, 56, 21, 11, 19, 45])
myprofit([7, 7, 9, 12, 20, 23, 34, 35, 46, 41, 39, 33, 31, 29, 42])