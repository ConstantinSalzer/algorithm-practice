class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for j in range (0,9):
            s = set()
            t = set()
            u = set()
            for i in range (0,9):
                if board[j][i] in s:
                    return False
                if board[j][i] != ".":
                    s.add(board[j][i])
                if board[i][j] in t:
                    return False
                if board[i][j] != ".":
                    t.add(board[i][j])
                
                row = (j // 3) * 3 + (i // 3)
                col = (j % 3) * 3 + (i % 3)
                if board[row][col] in u:
                    return False
                if board[row][col] != ".":
                    u.add(board[row][col])
        return True