class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if prices == []:
            return 0
        min = prices[0]
        res = 0
        for ele in prices:
            if ele < min:
                min = ele
            if ele - min > res:
                res = ele - min
        return res
