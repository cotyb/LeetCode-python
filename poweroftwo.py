class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n == 0:
            return False
        elif n == 1:
            return True
        while n != 1:
            k = n % 2
            n = n / 2
            if k == 1:
               return False
        return True

a = Solution()
for i in range(10000):
    if a.isPowerOfTwo(i):
        print i