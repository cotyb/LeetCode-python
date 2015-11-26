class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        transformation1 = {}
        transformation2 = {}
        if len(s) != len(t):
            return False
        for i in range(len(s)):
            if s[i] in transformation1:
                if t[i] != transformation1[s[i]]:
                    return False
            if t[i] in transformation2:
                if s[i] != transformation2[t[i]]:
                    return False
            else:
                transformation1[s[i]] = t[i]
                transformation2[t[i]] = s[i]
        return True


