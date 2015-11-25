class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        count = 0
        if not s:
            return 0
        s = s.strip()
        for char in s[-1::-1]:
            if char != " ":
                count += 1
            else:
                break

        return count

so = Solution()
print so.lengthOfLastWord("abc ")