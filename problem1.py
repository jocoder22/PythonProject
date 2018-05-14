def myprofit(prices_list):
    minprice = prices_list[0]

    maxprofit = 0

    for price in prices_list:
        minprice = min(minprice, price)
        profit = price - minprice
        maxprofit = max(maxprofit, profit)
    
    return maxprofit
