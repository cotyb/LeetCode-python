class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if not s:
            return ""
        if numRows == 1:
            return s
        result = [''for i in range(numRows)]
        base = numRows -2
        i = 0
        while i < len(s):
            j = 0
            while j < numRows and i < len(s):
                result[j] += s[i]
                j += 1
                i += 1
            j = base
            while j > 0 and i < len(s):
                result[j] += s[i]
                j -= 1
                i += 1
        res = ""
        for ele in result:
            res += ele
        return res
