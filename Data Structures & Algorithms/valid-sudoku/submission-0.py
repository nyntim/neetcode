class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in board:
            r = {}
            for num in row:
                if num == '.':
                    continue
                r[num] = r.get(num, 0) + 1
                if r[num] > 1: return False

        l = range(len(board))
        for i in l:
            c = {}
            for x in l:
                num = board[x][i]
                if num == '.': continue
                c[num] = c.get(num, 0) + 1
                if c[num] > 1: return False

        for box in range(9):
            b = {}
            box_row = (box // 3) * 3
            box_col = (box % 3) * 3
            for i in range(3):
                for j in range(3):
                    num = board[box_row + i][box_col + j]
                    if num == '.':
                        continue
                    b[num] = b.get(num, 0) + 1
                    if b[num] > 1:
                        return False        

        return True


