class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        left = 0
        while left < len(nums) - 1:
            while nums[left] != 0 and left < len(nums) - 1:
                left += 1
            right = left + 1
            while (right < len(nums) - 1 and nums[right] == 0):
                right += 1
            if left < len(nums) and right < len(nums):
                nums[left] = nums[right]
                nums[right] = 0
                left += 1


a = Solution()
print a.moveZeroes([0,1,0,3,12])


