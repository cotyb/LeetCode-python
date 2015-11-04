class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        cnt = 0
        can = 0
        for i in xrange(len(nums)):
            if cnt == 0:
                can = nums[i]
            if nums[i] == can:
                cnt += 1
            else:
                cnt -= 1
        return can

a = Solution()
print a.majorityElement([3,3,4])