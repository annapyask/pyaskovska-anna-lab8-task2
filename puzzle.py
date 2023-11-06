"""puzzle"""
def validate_board(board: list) -> bool:
    """
    Function that checks if the logic puzzle is correct
    >>> validate_board(["**** ****//n","***1 ****//n",\
"**  3****//n","* 4 1****//n","     9 5 //n"," 6  83  *//n",\
"3   1  **//n","  8  2***//n","  2  ****"])
    False
    """
    if len(board) != 9:
        return False
    for row in board:
        row_values = [i for i in row if i.isdigit()]
        if len(row_values) != len(set(row_values)):
            return False
    for col in range(9):
        col_values = [board[row][col] for row in range(9) if board[row][col].isdigit()]
        if len(col_values) != len(set(col_values)):
            return False
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            block = board[i][j:j + 3] + board[i + 1][j:j + 3] + board[i + 2][j:j + 3]
            block_values = [val for val in block if val.isdigit()]
            if len(block_values) != len(set(block_values)):
                return False
            
    return True


# print(validate_board([
#  "**** ****",
#  "***1 ****",
#  "**  3****",
#  "* 4 1****",
#  "     9 5 ",
#  " 6  83  *",
#  "3   1  **",
#  "  8  2***",
#  "  2  ****"
#  ]))  
if __name__ == "__main__":
   import doctest
   print(doctest.testmod())

