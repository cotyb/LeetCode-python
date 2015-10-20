#时间复杂度：O(N^3)
class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        result = []
        if nums < 4:
            return result
        nums.sort()
        for i in range(len(nums)-3):
            while (i != 0 and nums[i] == nums[i-1] and i < j-2):
                i += 1
            j = len(nums) - 1
            temp1 = nums[i]
            while i < j - 2:
                while (j != len(nums)-1 and nums[j] == nums[j+1] and i < j-2):
                    j -= 1
                temp2 = nums[j]
                left = i + 1
                right = j -1
                while left < right:
                    while (left < right and nums[left] == nums[left - 1]):
                        left += 1
                    while (left > right and nums[right] == nums[right + 1]):
                        right -= 1
                    temp3 = nums[left]
                    temp4 = nums[right]
                    addition = temp1 + temp2 + temp3 + temp4
                    if addition < target:
                        left += 1
                    elif addition > target:
                        right -= 1
                    else:
                        left += 1
                        right -= 1
                        tmp = [temp1, temp3, temp4, temp2]
                        result.append(tmp)
                j -= 1
        return result

a = Solution()
print a.fourSum([-497,-488,-488,-484,-463,-463,-442,-402,-397,-394,-384,-380,-361,-358,-355,-350,-344,-338,-333,-330,-328,-325,-305,-301,-292,-290,-272,-262,-220,-202,-189,-172,-166,-162,-137,-133,-121,-90,-69,-68,-55,-51,-50,-44,-44,-38,-36,-14,-4,15,22,38,75,91,110,148,155,157,160,166,170,191,205,215,219,223,223,235,255,267,277,280,282,300,314,315,330,361,393,412,419,461,478,497],-2057)
