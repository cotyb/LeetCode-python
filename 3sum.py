class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []
        if (len(nums) < 3):
            return result
        nums.sort()
        print nums
        for i in range(len(nums)-2):
            if (i != 0 and nums[i] == nums[i-1]):
                continue
            temp1 = nums[i]
            left = i + 1
            right = len(nums) - 1
            while left < right:
                temp2 = nums[left]
                temp3 = nums[right]
                addition = temp1 + temp2 + temp3
                if addition > 0:
                    right -= 1
                    while nums[right] == nums[right+1] and left < right:
                        right -= 1
                elif addition < 0:
                    left += 1
                    while nums[left] == nums[left-1] and left < right:
                        left += 1
                else:
                    tmp = [temp1,temp2,temp3]
                    result.append(tmp)
                    left += 1
                    right -= 1
                    while nums[right] == nums[right+1] and left < right:
                        right -= 1
                    while nums[left] == nums[left-1] and left < right:
                        left += 1
        return result

a = Solution()

print a.threeSum([0,0,0])