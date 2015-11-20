class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        k = rowIndex + 1
        index = 0
        result = [0] * k
        result[0] = 1
        while index < k:
            for i in range(index ,0,-1):
                result[i] = result[i-1] + result[i]
            index += 1
        return result

a = Solution()
print a.getRow(0)


