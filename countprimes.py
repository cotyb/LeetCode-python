import math
class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        res = [True for i in range(n)]
        i = 2
        while i < math.sqrt(n):
            if not res[i]:
                i += 1
                continue
            j = i * i
            while j < n:
                res[j] = False
                j += i
            i += 1

        count = 0
        for i in range(2,n):
            if res[i] == True:
                count += 1
        return count

so = Solution()
print so.countPrimes(20)