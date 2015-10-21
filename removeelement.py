class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        left = 0
        right = len(nums) - 1
        count = 0
        while left <= right:
            while nums[left] == val and left <= right and right >= 0:
                count += 1
                nums[left] = nums[right]
                right -= 1
            left += 1
        nums = nums[:len(nums) - count]
        return len(nums)

a = Solution()
print a.removeElement([4,5],5)