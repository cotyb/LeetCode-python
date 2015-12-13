class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        bitmap = 0
        for num in nums:
            bitmap += 2 ** num
        res = 0
        while bitmap & 1 == 1:
            res += 1
            bitmap = bitmap >> 1
        return res
