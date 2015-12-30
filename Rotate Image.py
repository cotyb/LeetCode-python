class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        length = len(matrix)
        layers = (length - 1)/2
        for i in range(layers + 1):
            for j in range(i,length-1-i):
                tmp = matrix[i][j]
                matrix[i][j] = matrix[length-1-j][i]
                matrix[length-1-j][i] = matrix[length-1-i][length-1-j]
                matrix[length-1-i][length-1-j] = matrix[j][length-1-i]
                matrix[j][length-1-i] = tmp


so = Solution()
so.rotate([[1,2],[3,4]])