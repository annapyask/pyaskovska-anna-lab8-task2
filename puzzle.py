"""puzzle"""
def validate_board(board: list) -> bool:
    """
    Function that checks if the logic puzzle is correct
    function on git: https://github.com/annapyask/pyaskovska-anna-lab8-task2.git
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
    return True

if __name__ == "__main__":
   import doctest
   print(doctest.testmod())

