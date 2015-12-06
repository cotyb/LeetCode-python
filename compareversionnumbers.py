class Solution(object):
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        ver1 = version1.split('.')
        ver2 = version2.split('.')
        length1 = len(ver1)
        length2 = len(ver2)
        if length1 <= length2:
            return self.compare(ver1,ver2,length1)
        return -1*self.compare(ver2,ver1,length2)

    def compare(self,ver1,ver2,length):
        i = 0
        while i < length and int(ver1[i]) == int(ver2[i]):
            i += 1
        if i == length:
            for ele in ver2[i:]:
                if int(ele) != 0:
                    return -1
            return 0
        else:
            if int(ver1[i]) > int(ver2[i]):
                return 1
            elif int(ver1[i]) < int(ver2[i]):
                return -1


so = Solution()
print so.compareVersion("100.9","1000.0")