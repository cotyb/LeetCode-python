class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        result = [1] * len(nums)
        for i in xrange(1,len(nums)):
            result[i] = result[i-1] * nums[i-1]
        result[0] = 1
        tmp = 1
        for i in xrange(len(nums)-2,-1,-1):
            tmp = tmp * nums[i+1]
            result[i] = result[i] * tmp
        return result

a = Solution()
print a.productExceptSelf([1,2,3,4])