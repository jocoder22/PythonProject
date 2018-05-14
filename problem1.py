import operator

def myprofit(prices_list):
    minprice = prices_list[0]

    maxprofit = 0

    for price in prices_list:
        minprice = min(minprice, price)
        profit = price - minprice
        maxprofit = max(maxprofit, profit)

    return maxprofit


def dailyMargin(prices_day):

    max_margin = 0
    margin_list = {}

    for i in range(len(prices_day) - 1):
        price_diff = abs(prices_day[i] - prices_day[i+1])
        margin_list['Day '+str(1+i)] = price_diff
        max_margin = max(max_margin, price_diff)

    max_dic = max(margin_list.items(), key=operator.itemgetter(1))

    return max_dic, margin_list


myprofit([10, 23, 22, 56, 21, 11, 19, 45])
myprofit([7, 7, 9, 12, 20, 23, 34, 35, 46, 41, 39, 33, 31, 29, 42])