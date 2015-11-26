class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        if k >= len(nums):
            k = len(nums) - 1
        for i in range(len(nums)):
            if i + k >= len(nums):
                upper = len(nums)
            else:
                upper = i + k + 1
            for j in range(i+1,upper):
                if nums[i] == nums[j]:
                    return True
        return False


so = Solution()
nums = [1,2,7,4,5,6,7,8,9,9]
print so.containsNearbyDuplicate(nums,3)