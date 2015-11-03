class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        cnt = {}
        for char in s:
            if char in cnt:
                cnt[char] += 1
            else:
                cnt.setdefault(char,1)
        for char in t:
            if not char in cnt:
                return False
            else:
                cnt[char] -= 1
        for key in cnt:
            if cnt[key] != 0:
                return False
        return True


