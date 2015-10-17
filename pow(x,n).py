class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        isNegtive = 0
        if n == 1:
            return x
        if n == 0:
            return 1
        if n < 0:
            isNegtive = 1

        if isNegtive:
            n = -n
            k = n/2
            r = n - k * 2
            temp1 = self.myPow(x,k)
            temp2 = self.myPow(x,r)
            return 1.0/(temp1*temp1*temp2)
        else:
            k1 = n /2
            print k1
            k2 = n - k1 * 2
            print k2
            temp1 = self.myPow(x,k1)
            temp2 = self.myPow(x,k2)
            return temp1*temp1*temp2

a = Solution()
print a.myPow(9.5,2)