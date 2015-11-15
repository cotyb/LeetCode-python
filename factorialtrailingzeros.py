class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        x = 5
        result = 0
        while n > x:
            result += n / x
            x *= 5
        return result