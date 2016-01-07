class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return nums[0]
        start = 0
        end = len(nums) - 1
        while start < end:
            mid = (start + end)/2
            if nums[start] <= nums[end]:
                return nums[start]
            elif nums[mid] >= nums[end]:
                start = mid + 1
            else:
                end = mid
        return nums[start]

so = Solution()
print so.findMin([4, 5, 6, 7, 0, 1, 2])