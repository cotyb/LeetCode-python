class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        if m <= 0 or n <= 0:
            return 0
        res = [[0 for col in range(n)] for row in range(m)]
        for row in range(m):
            res[row][0] = 1
        for col in range(n):
            res[0][col] = 1
        for i in range(1,m):
            for j  in range(1,n):
                res[i][j] = res[i-1][j] + res[i][j-1]

        return res[m-1][n-1]

so = Solution()
so.uniquePaths(3,4)
