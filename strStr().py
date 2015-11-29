class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if not haystack and not needle:
            return 0
        if not haystack or len(needle) > len(haystack):
            return -1
        if not needle:
            return 0
        else:
            i = 0
            while i < len(haystack)-len(needle)+1:
                tmp = i
                for j in range(len(needle)):
                    if i < len(haystack)-len(needle)+1 and haystack[i+j] != needle[j] :
                        i += 1
                if tmp == i:
                    return tmp
            return -1