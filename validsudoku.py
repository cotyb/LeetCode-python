class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        for row in board:
            if not self.isvalidrow(row):
                return False
        for i in range(len(board)):
            tmp = ''
            for j in range(len(board)):
                tmp += board[j][i]
                if not self.isvalidrow(tmp):
                    return False
        for i in range(1,len(board)-1, 3):
            for j in range(1,len(board)-1,3):
                tmp = ''
                for m in range(-1,2,1):
                    for n in range(-1,2,1):
                        tmp += board[i+m][j+n]
                        if not self.isvalidrow(tmp):
                            return False
        return True



    def isvalidrow(self,str):
        tmp = ''
        for ele in str:
            tmp += ele
        p = tmp.replace('.','')
        if len(set(p)) == len(p):
            return True
        return False

so = Solution()
print so.isValidSudoku([".87654321","2........","3........","4........","5........","6........","7........","8........","9........"])