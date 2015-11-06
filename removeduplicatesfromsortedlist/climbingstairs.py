class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 1:
            return 1
        elif n == 2:
            return 2
        else:
            a, b, c = 1, 2, 3
            for i in range(3,n+1):
                c = a+b
                a = b
                b = c
            return c