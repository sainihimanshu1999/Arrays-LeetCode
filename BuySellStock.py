'''
This question is pretty easy, in this we create two variable and count min price and max profit 
'''

def buyandsell(self,prices):
    max_profit,min_price = 0, float('inf')
    for price in prices:
        min_price = min(min_price,price)
        profit = price - min_price
        max_profit = max(max_profit,profit)
    return max_profit