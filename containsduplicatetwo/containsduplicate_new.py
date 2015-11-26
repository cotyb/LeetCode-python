class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        num_index = {}
        length = len(nums)
        for i in range(length):
            index = num_index.get(nums[i])
            if index >= 0 and i - index <= k:
                return True
            num_index[nums[i]] = i
        return False
