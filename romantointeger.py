class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        TABLE = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}
        result = 0
        num = 0
        for i in xrange(len(s)-1):
            cur = TABLE[s[i]]
            next = TABLE[s[i+1]]
            if cur >= next:
                num += cur
            else:
                num -= cur
        num += TABLE[s[-1]]

        return num

a = Solution()
print a.romanToInt("IX")

