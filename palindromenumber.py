class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        elif x == 0:
            return True
        base = 1
        while x /10**base:
            base += 1
        while x:
            if x/10**(base-1) == x%10:
                x = x % 10**(base-1)
                x = x / 10
                base -= 2
            else:
                return False
        return True

a = Solution()
print a.isPalindrome(2)


