class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sum = nums[0]
        res = nums[0]
        for ele in nums[1:]:
            if sum < 0:
                sum = 0
            sum += ele
            res = max(sum, res)
        return res
