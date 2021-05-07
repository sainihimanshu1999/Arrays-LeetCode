'''
In this question we are only allwoed to do the transaction 2 times, hence first time we move forward and
then the second time we move backward
'''

def buyandsell(self,prices):

    #moving forward
    min_price,max_profit = float('inf'),0
    profits = []

    for price in prices:
        min_price = min(price,min_price)
        profit = price - min_price
        max_profit = max(max_profit,profit)
        profits.append(max_profit)


    #moving backward

    max_price,total_max,max_profit = float('-inf'),0,0

    for i in range(len(prices))[::-1]:
        max_price = max(prices[i],max_price)
        profit = max_price-prices[i]
        max_profit = max(max_profit,profit)
        total_max = max(total_max, max_profit+profits[i])

    return total_max