#时间复杂度：O(N^2)
class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        result = []
        count = {}
        hash_table = {}
        if len(nums) < 4:
            return result
        nums.sort()
        i = 0
        while i < len(nums):
            j = i + 1
            while j < len(nums):
                key = nums[i] + nums[j]
                if hash_table.has_key(key):
                    hash_table[key] = hash_table[key] + [nums[i], nums[j]]
                else:
                    hash_table[key] = [nums[i], nums[j]]
                j += 1
                while (j < len(nums) and nums[j-1] == nums[j]):
                    j += 1
            i += 1
            while (i < len(nums) and nums[i-1] == nums[i]):
                i += 1
        for element in nums:
            if count.has_key(element):
                count[element] += 1
            else:
                count[element] = 1
        keys = hash_table.keys()
        for element in keys:
            if not hash_table.has_key(target - element):
                continue
            elif element > target - element:
                continue
            for i in range(0,len(hash_table[element]),2):
                for j in range(0,len(hash_table[target - element]),2):
                    if max(hash_table[element][i], hash_table[element][i+1]) <= min(hash_table[target - element][j], hash_table[target - element][j+1]):
                        flag = True
                        count[hash_table[element][i]] -= 1
                        count[hash_table[element][i+1]] -= 1
                        count[hash_table[target - element][j]] -= 1
                        count[hash_table[target - element][j+1]] -= 1
                        if count[hash_table[element][i]] <0 or count[hash_table[element][i+1]] < 0 or count[hash_table[target - element][j]] < 0 or count[hash_table[target - element][j+1]] < 0:
                            flag = False
                        count[hash_table[element][i]] += 1
                        count[hash_table[element][i+1]] += 1
                        count[hash_table[target - element][j]] += 1
                        count[hash_table[target - element][j+1]] += 1

                        if(flag):
                            tmp = [hash_table[element][i], hash_table[element][i+1], hash_table[target - element][j], hash_table[target - element][j+1]]
                            result.append(tmp)
        return result
a = Solution()
print a.fourSum([-1,0,1,2,-1,-4],-1)
