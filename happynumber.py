class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n < 1:
            return False
        elif n == 1:
            return True
        loop = []
        loop.append(n)
        while True:
            s = 0
            while n:
                s += (n % 10)*(n % 10)
                n /= 10
            if s == 1:
                return True
            else:
                if s in loop:
                    return False
                loop.append(s)
                n = s

a = Solution()
print a.isHappy(2)