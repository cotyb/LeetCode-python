class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        result = 0
        for i in xrange(len(s)):
            tmp = ord(s[i]) - ord('A') + 1
            result = result * 26 + tmp
        return result


a = Solution()
print a.titleToNumber("AB")
