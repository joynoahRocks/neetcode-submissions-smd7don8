class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # def valid(row,col):
        #     for i in range(9):
        #         if i != row and board[i][col] == board[row][col]:
        #             return False
        #     for j in range(9):
        #         if j != col and board[row][j] == board[row][col]:
        #             return False
        #     actRow = (row//3) * 3
        #     actCol = (col//3) * 3
        #     for i in range(actRow,actRow + 3):
        #         for j in range(actCol,actCol + 3):
        #             if board[i][j] == board[row][col]:
        #                 if i == row and j == col:
        #                     continue
        #                 else:
        #                     return False
        #     return True 


        # for i in range(9):
        #     for j in range(9):
        #         if board[i][j] != ".":
        #             if not valid(i,j):
        #                 return False
        # return True
        rows = [0] * 9
        cols = [0] * 9
        box = [0] * 9

        for i in range(9):
            for j in range(9):
                if board[i][j] == ".":
                    continue
                
                mask = 1 << int(board[i][j])
                box_ind = (i//3) * 3 + (j//3) 
                if (rows[i] & mask) or (cols[j] & mask) or (box[box_ind] & mask):
                    return False
                
                rows[i] |= mask
                cols[j] |= mask
                box[box_ind] |= mask
        return True