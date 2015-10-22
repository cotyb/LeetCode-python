class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return None
        else:
            result = nums[0]
            for i in range(1,len(nums)):
                result = result ^ nums[i]
            return result


a = Solution()
print a.singleNumber([1,2,1,0,0,2,3])