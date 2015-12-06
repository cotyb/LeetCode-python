class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        length = len(nums)
        tmp = []
        for i in range(length):
            tmp.append(nums[i])
        if k >= len(nums):
            k = k % length
        if k == 0:
            pass
        else:
            for i in range(length):
                nums[i] = tmp[(i-k)%length]
