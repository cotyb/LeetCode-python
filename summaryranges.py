class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        nums.append(-1)
        res = []
        if not nums:
            return []
        i = 0
        while i < len(nums) - 1:
            start = nums[i]
            while i < len(nums) - 1 and nums[i] + 1 == nums[i+1]:
                i += 1
            stop = nums[i]
            i += 1
            if start == stop:
                res.append(str(start))
            else:
                res.append(str(start)+'->'+str(stop))
        return res
