    def maxProfit(self, prices):
        l , r = 0 , 1
        max_profit = 0
        while r < len(prices):
            if prices[r]>prices[l]:
                cp = prices[r]-prices[l]
                max_profit = max(cp,max_profit)
            else:
                l = r
            r +=1
        return max_profit

# similar approach
def max_profit(prices):
    min_price = float('inf')
    max_profit = 0

    for price in prices:
        if price < min_price:
            min_price = price
        else:
            max_profit = max(max_profit, price - min_price)

    return max_profit


