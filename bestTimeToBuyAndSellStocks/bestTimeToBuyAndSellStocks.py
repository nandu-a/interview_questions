import math

def maxProfit(prices) -> int:
    
    profit = 0
    minimum = math.inf
        
    for price in prices:
        if price < minimum:
            minimum = price
        elif price - minimum > profit:
            profit = price - minimum
        
    return profit

print(maxProfit([7,1,5,3,6,4]))

