class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ''
        common = strs[0]
        for element in strs[1:]:
            i = 0
            while i < len(common) and i < len(element) and common[i] == element[i]:
                i += 1
            common = common[:i]
            if not common:
                return ''
        return common
so = Solution()
print so.longestCommonPrefix(['abc','',''])