class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 1:
            return 1
        result = [0] * (n+1)
        result[0] = 1
        result[1] = 1
        i = 2
        while i <= n:
            for j in range(i):
                result[i] += result[j]*result[i-j-1]
            i += 1
        return result[-1]
so = Solution()
print so.numTrees(3)
