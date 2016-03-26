from copy import deepcopy
import numpy as np
import Cell

def simulation(individual,time):

    def changeLights(index,board,individual):
        # 1
        board[0][3].open = 1 if individual[0][index]==1 else 0
        board[2][3].open = 0 if individual[0][index]==1 else 1
        # 2
        board[0][8].open = 1 if individual[1][index]==1 else 0
        board[3][3].open = 0 if individual[1][index]==1 else 1
        # 3
        board[1][3].open = 1 if individual[2][index]==1 else 0
        board[2][8].open = 0 if individual[2][index]==1 else 1
        # 4
        board[1][8].open = 1 if individual[3][index]==1 else 0
        board[3][8].open = 0 if individual[3][index]==1 else 1
        return board

    def printBoard(board):
        import PrintBoard
        PrintBoard.printBoard(board)

    inputCars=0
    index=0
    board = Cell.getDefaultConfiguration()
    for i in range(time):
        if (i%5==0):
            board[0][0].addCar();board[1][0].addCar();board[2][0].addCar();board[3][0].addCar();
            inputCars+=4
        if (i%10==0):
            board = deepcopy(changeLights(index,board,individual))
            index+=1
        newBoard = deepcopy(board)

        # Intersection
        newBoard[3][4].actualize(board[0][8],board[3][3],board[0][10],board[3][5])
        newBoard[3][9].actualize(board[1][8],board[3][8],board[1][10],board[3][10])
        newBoard[2][4].actualize(board[0][3],board[2][3],board[0][5],board[2][5])
        newBoard[2][9].actualize(board[1][3],board[2][8],board[1][5],board[2][10])
        for j in range(0,len(board),1):
            for k in range(len(board[0])):
                if (k==0):
                    newBoard[j][k].actualize(board[j][k+1])
                if (k==1 or k==2 or k==6 or k==7 or k==11 or k==12):
                    newBoard[j][k].actualize(board[j][k-1],board[j][k+1])
                if (k==3 or k==8):
                    newBoard[j][k].actualize(board[j][k-1],board[j][k+1])
                if (k==5 or k==10):
                    if (j<=1):
                        newBoard[j][k].actualize(board[j][k-1],board[j][k+1],True)
                    else:
                        newBoard[j][k].actualize(board[j][k-1],board[j][k+1],False)
                if (k==13):
                    newBoard[j][k].actualize(board[j][k-1])
        # copy new board
        board = deepcopy(newBoard)
    fit = (board[0][13].getOutput() + board[1][13].getOutput() + board[2][13].getOutput() + board[3][13].getOutput())
    return float(fit)/float(inputCars)

def fitness(population,time):
    fitnessValues = np.zeros(population.shape[0])
    for i in range(population.shape[0]):
        fitnessValues[i] = simulation(population[i],time)
    return fitnessValues