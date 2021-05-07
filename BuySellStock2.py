'''
In this question we don't have to consider max profit, just how much profit we can make by multiple 
transaction
'''

def buyandsell(self,prices):
    profit = 0
    for i in range(len(prices)-1):
        profit += max((prices[i+1]-prices[i]),0)

    return profit