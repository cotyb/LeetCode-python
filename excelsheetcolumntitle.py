class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        result = ""
        while n > 0:
            tmp = (n-1) % 26
            n = (n-1) / 26
            result = chr(tmp+ord('A')) + result
        return result

a = Solution()
print a.convertToTitle(1)

