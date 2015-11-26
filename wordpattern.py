class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        str = str.split(' ')
        trans1 = {}
        trans2 = {}
        if len(pattern) != len(str):
            return False
        for i in range(len(pattern)):
            trans1[pattern[i]] = trans1.get(pattern[i],str[i])
            if trans1[pattern[i]] != str[i]:
                return False
            trans2[str[i]] = trans2.get(str[i],pattern[i])
            if trans2[str[i]] != pattern[i]:
                return False
