class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        cnt = 0
        while n > 0:
            tmp = n % 2
            n = n/2
            cnt += tmp

        return cnt

a = Solution()
print a.hammingWeight(-1)