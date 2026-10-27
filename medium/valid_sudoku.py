from collections import defaultdict

board = [["1","2",".",".","3",".",".",".","."],
 ["4",".",".","5",".",".",".",".","."],
 [".","9","8",".",".",".",".",".","3"],
 ["5",".",".",".","6",".",".",".","4"],
 [".",".",".","8",".","3",".",".","5"],
 ["7",".",".",".","2",".",".",".","6"],
 [".",".",".",".",".",".","2",".","."],
 [".",".",".","4","1","9",".",".","8"],
 [".",".",".",".","8",".",".","7","9"]]

def isValidSudoku(board):
    columns = defaultdict(list)
    rows = defaultdict(list)
    groups = defaultdict(list)
    for row in range(9):
        for column in range(9):
            number = board[row][column]
            if number.isdigit():
                if (number in columns[column] or
                    number in rows[row] or 
                    number in groups[row//3, column//3]):

                    return False
                rows[row].append(number)
                columns[column].append(number)
                groups[row//3, column//3].append(number)

    return True
    

if __name__ == "__main__":
    print(isValidSudoku(board))