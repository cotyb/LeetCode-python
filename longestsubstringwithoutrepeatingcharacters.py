class Solution:
    # @param {string} s
    # @return {integer}
    def lengthOfLongestSubstring(self, s):
        substring = {}
        count = 0
        flag = 0
        for i, str in enumerate(s):
            if str in substring and substring[str] >= flag:
                flag = substring[str] + 1
            substring[str] = i
            count = max(count, i - flag + 1)
        return count