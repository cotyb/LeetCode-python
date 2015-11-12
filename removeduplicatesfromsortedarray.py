class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        length = 0
        index = 0
        if nums == [] or len(nums) == 1:
            return len(nums)
        else:
            while index < len(nums):
                nums[length] = nums[index]
                index += 1
                while index < len(nums)  and nums[index] == nums[index-1]:
                    index += 1
                length += 1

        return length


a = Solution()
print a.removeDuplicates([1,1,2,2,2,22])