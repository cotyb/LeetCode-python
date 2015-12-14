class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left = 0
        right = len(nums) - 1
        while target != nums[(left+right)/2] and left != right:
            if target > nums[(left+right)/2]:
                left = (left + right)/2 + 1
            else:
                right = (left + right)/2
        if target > nums[(left+right)/2]:
            return (left + right)/2 + 1
        return (left + right)/2


li = [1,2,3,5]
so = Solution()
print so.searchInsert([1,3,5,6], 0 )