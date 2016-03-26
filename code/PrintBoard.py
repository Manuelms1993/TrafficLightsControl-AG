import sys
def printBoard(board):
    for i in range(len(board)):
        for j in range(len(board[i])):
            if j==4 or j==9:
                if (board[i][j].takenV):
                    s = "V" if (board[i][j].takenV) else "_"
                else:
                    s = "H" if (board[i][j].takenH) else "_"
                sys.stdout.write(str(s)+",")
            else:
                s = "X" if (board[i][j].taken) else "_"
                sys.stdout.write(str(s)+",")
        print
    print
