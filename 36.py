class Solution:
    def rowcheck(self,board)->bool:
        res=True
        for i in range(9):
            m={}
            for j in range(9):
                if board[i][j]!="." and board[i][j] not in m:
                    m[board[i][j]]=1
                elif board[i][j]!=".":
                    m[board[i][j]]=m[board[i][j]]+1
            for x in m:
                if m[x]!=1:
                    res=False
        return res
    def checkcolumn(self,board)->bool:
        res=True
        for i in range(9):
            m={}
            for j in range(9):
                if board[j][i]!="." and board[j][i] not in m:
                    m[board[j][i]]=1
                    
                elif board[j][i]!=".":
                        m[board[j][i]]+=1
            for x in m:
                if m[x]!=1:
                    res=False
        return res
    
    def check_matrix(self, board):
        res = True
        for start_row in range(0, 9, 3):
            for start_col in range(0, 9, 3):
                m = {}
                for i in range(start_row, start_row + 3):
                    for j in range(start_col, start_col + 3):
                        if board[i][j] != "." and board[i][j] not in m:
                            m[board[i][j]] = 1
                        elif board[i][j] != ".":
                            m[board[i][j]] += 1
                        if m.get(board[i][j], 0) > 1:
                            res = False
                            break
                    if not res:
                        break
                if not res:
                    break
        return res

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        return self.check_matrix(board) and self.rowcheck(board) and self.checkcolumn(board)
