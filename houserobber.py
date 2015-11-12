class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        using dynamic programming
        maxv[i] = max(maxv[i-1],maxv[i-2]+nums[i])
        """
        length = len(nums)
        result = [0] * length
        if length == 0:
            return 0
        elif length == 1:
            return nums[0]
        else:
            result[0] = nums[0]
            result[1] = max(nums[1],nums[0])
            for i in xrange(2,length):
                result[i] = max(result[i-1], result[i-2]+nums[i])
            return result[length-1]

a = Solution()
print a.rob([1,2,3,4,5,6,4,3,2,1,2,3,4,5,6,7,84,22,1])