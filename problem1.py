import operator


def myprofit(prices_list):
    minprice = prices_list[0]

    maxprofit = prices_list[1] - prices_list[0]

    for price in prices_list:
        minprice = min(minprice, price)
        profit = price - minprice
        maxprofit = max(maxprofit, profit)

    return maxprofit


def dailyMargin(prices_day):

    max_margin = 0
    margin_list = {}

    for i in range(len(prices_day) - 1):
        price_diff = prices_day[i+1] - prices_day[i]
        margin_list['Day '+str(1+i)] = price_diff
        max_margin = max(max_margin, price_diff)

    max_dic = max(margin_list.items(), key=operator.itemgetter(1))

    return max_dic, margin_list


def profit2(stock_prices):
    if len(stock_prices) < 2:
        raise Exception('Need at least two stock prices')

    min_price = stock_prices[0]
    max_profit = stock_prices[1] - stock_prices[0]

    for price in stock_prices[1:]:
        profitc = price - min_price
        max_profit = max(max_profit, profitc)
        min_price = min(min_price, price)

    return max_profit


myprofit([10, 23, 22, 56, 21, 11, 19, 45])
myprofit([7, 7, 9, 12, 20, 23, 34, 35, 46, 41, 39, 33, 31, 29, 42])
dailyMargin([779, 822, 720, 723, 834, 835, 846, 841])
dailyMargin([71, 75, 79, 72, 70, 73, 74, 75, 76, 71])
