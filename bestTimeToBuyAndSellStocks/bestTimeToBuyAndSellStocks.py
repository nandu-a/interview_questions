# Time Complexity - O(n)
# Space Complexity - O(1)

import math

def maxProfit(prices) -> int:
    
    profit = 0
    minimum = math.inf
        
    for price in prices:
        if price < minimum:
            minimum = price  # minimum value is updated when the value is lesser than price
        elif price - minimum > profit:
            profit = price - minimum
        
    return profit  # integer is returned

print(maxProfit([7,1,5,3,6,4]))

