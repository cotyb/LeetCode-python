class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        length = len(prices)
        if length == 0:
            return 0
        i = 1
        res = 0
        while i < length:
            if prices[i] > prices[i-1]:
                res += prices[i] - prices[i-1]
            i += 1
        return res


