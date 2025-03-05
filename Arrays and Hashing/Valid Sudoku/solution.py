class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        def check_rows() -> bool:
            for row in board:
                counts = [0] * 10
                for str_num in row:
                    if str_num == ".": continue
                    num = int(str_num)
                    counts[num] += 1
                    if counts[num] > 1: return False
            
            return True
        
        def check_cols() -> bool:
            for col in zip(*board):
                counts = [0] * 10
                for str_num in col:
                    if str_num == ".": continue
                    num = int(str_num)
                    counts[num] += 1
                    if counts[num] > 1: return False
            
            return True
        
        def check_sub_box(start_row, start_col) -> bool:
            counts = [0] * 10
            for row in range(start_row, start_row+3):
                for col in range(start_col, start_col+3):
                    str_num = board[row][col]
                    if str_num == ".": continue
                    num = int(str_num)
                    counts[num] += 1
                    if counts[num] > 1: return False
            
            return True

        def check_sub_boxes() -> bool:
            start_rows = [0, 3, 6]
            start_cols = [0, 3, 6]
            for start_row in start_rows:
                for start_col in start_cols:
                    if not check_sub_box(start_row, start_col):
                        return False
            
            return True
        
        return check_rows() and check_cols() and check_sub_boxes()
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        def check_rows() -> bool:
            for row in board:
                counts = [0] * 10
                for str_num in row:
                    if str_num == ".": continue
                    num = int(str_num)
                    counts[num] += 1
                    if counts[num] > 1: return False
            
            return True
        
        def check_cols() -> bool:
            for col in zip(*board):
                counts = [0] * 10
                for str_num in col:
                    if str_num == ".": continue
                    num = int(str_num)
                    counts[num] += 1
                    if counts[num] > 1: return False
            
            return True
        
        def check_sub_box(start_row, start_col) -> bool:
            counts = [0] * 10
            for row in range(start_row, start_row+3):
                for col in range(start_col, start_col+3):
                    str_num = board[row][col]
                    if str_num == ".": continue
                    num = int(str_num)
                    counts[num] += 1
                    if counts[num] > 1: return False
            
            return True

        def check_sub_boxes() -> bool:
            start_rows = [0, 3, 6]
            start_cols = [0, 3, 6]
            for start_row in start_rows:
                for start_col in start_cols:
                    if not check_sub_box(start_row, start_col):
                        return False
            
            return True
        
        return check_rows() and check_cols() and check_sub_boxes()


from collections import defaultdict
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        cols = defaultdict(set)
        sub_boxes = defaultdict(set)

        for row in range(9):
            for col in range(9):
                if board[row][col] == ".":
                    continue
                
                if ( 
                    board[row][col] in rows[row] 
                    or board[row][col] in cols[col]
                    or board[row][col] in sub_boxes[(row // 3, col // 3)]
                ):
                    return False
                
                rows[row].add(board[row][col])
                cols[col].add(board[row][col])
                sub_boxes[(row // 3, col //3)].add(board[row][col])
            
        return True


# * BIT MASKING IS SPACE OPTIMIZED

# 2^1 => 2.
# (1 << val)  //     1<<1   =>  10(binary)
# (checker & (1 << val))
# if (checker & (1 << val)) > 0: return False - if the bit is already set, then return False - already present
# checker |= (1 << val) - set the bit

from collections import defaultdict
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [0] * 9
        cols = [0]  * 9
        sub_boxes = [0] * 9

        for row in range(9):
            for col in range(9):
                if board[row][col] == ".":
                    continue
                
                num = int(board[row][col]) - 1
                if ( 
                    (1 << num) & rows[row] 
                    or (1 << num) & cols[col]
                    or (1 << num) & sub_boxes[(row // 3) * 3 + (col // 3)]
                ):
                    return False
                
                rows[row] |= (1 << num)
                cols[col] |= (1 << num)
                sub_boxes[(row // 3) * 3 + (col // 3)] |= (1 << num)
            
        return True
