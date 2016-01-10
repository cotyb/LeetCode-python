import math
class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        return False if n <= 0 else n == pow(3, round(math.log(n, 3)))


so = Solution()
print so.isPowerOfThree(3)
        