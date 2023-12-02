class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """

        s = 0 #slow pointer
        f = 1 #fast tpointer

        maxProfit = 0 #maximum profit

        while(f < len(prices)):
            if prices[f] < prices[s]:
                s = f
            
            else:
                if maxProfit < (prices[f] - prices[s]):
                    maxProfit = prices[f] - prices[s]
                
            f += 1

        return maxProfit

class Solution2(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """

        l = 0
        r = 0
        maxp = 0

        for i in range(len(prices)):
            maxp = max(maxp, prices[r] - prices[l])
            if prices[r] < prices[l]:
                l = r

            r += 1

        return maxp