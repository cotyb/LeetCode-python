class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        self.result = []
        tmp = []
        self.dfs(n,k,1,0,tmp)
        return self.result

    def dfs(self,n,k,m,p,tmp):
        if p == k:
            self.result.append(tmp[:])
            return
        else:
            for i in range(m,n+1):
                tmp.append(i)
                self.dfs(n,k,i+1,p+1,tmp)
                tmp.pop()

a = Solution()
print a.combine(4,2)