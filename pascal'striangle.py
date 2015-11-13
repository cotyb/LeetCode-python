class Solution:
    # @return a list of lists of integers
    def generate(self, numRows):
        ret = []
        for i in range(numRows):
            ret.append([1])
            for j in range(1,i+1):
                if j==i:
                    ret[i].append(1)
                else:
                    ret[i].append(ret[i-1][j]+ret[i-1][j-1])
        return ret


a = Solution()
print a.generate(0)