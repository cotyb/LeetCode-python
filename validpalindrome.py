class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if not s:
            return True
        i, j = 0, len(s)-1
        while i < j:
            while i < len(s)-1 and not ((s[i] >= '0' and s[i] <= '9') or (s[i] >= 'a' and s[i] <= 'z') or (s[i] >= 'A' and s[i] <= 'Z')):
                i += 1
            while j >= 0 and not ((s[j] >= '0' and s[j] <= '9') or (s[j] >= 'a' and s[j] <= 'z') or (s[j] >= 'A' and s[j] <= 'Z')):
                j -= 1
            if s[i].lower() == s[j].lower():
                i += 1
                j -= 1
            else:
                return False
        return True

so = Solution()
print so.isPalindrome(".,")