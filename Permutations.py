class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        if len(nums) == 1:
            return [nums]
        for i in range(len(nums)):
            tmp = self.permute(nums[:i] + nums[i+1:])
            for ele in tmp:
                res.append([nums[i]]+ele)
        return res


so = Solution()
print so.permute([1,2,3])