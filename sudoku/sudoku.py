'''
Euler problem 96
https://projecteuler.net/problem=96
'''

'''
    Print sudoku table
'''
def printTable(table):
    for row in table:
        for col in row:
            print col, 
        print ""


'''
    Check if num apperas in a specific row
'''
def numInRow(row, num):
    for n in sudokuTable[row]:
        if num == n:
            return True
    return False


'''
    Check if num appears in a specific column
'''
def numInCol(col, num):
    for row in sudokuTable:
        if row[col] == num:
            return True
    return False

'''
    Check if num appears in a box, 3x3 grid
'''
def numInBox(boxStartRow, boxStartCol, num):
    for row in range(0,3):
        for col in range(0,3):
            if(sudokuTable[row+boxStartRow][col+boxStartCol] == num):
                return True
    return False

'''
    Check if still exists empty spots
'''
def findEmptySpot():
    for row in range(0,9):
        for col in range(0,9):
            if sudokuTable[row][col] == 0:
                return row, col
    return False

def isSafe(row, col, num):
    if numInRow( row, num) == False and numInCol(col, num) == False and numInBox(row - row%3, col -col%3, num) == False:
        return True

    return False

def solve():
    freeSpot = findEmptySpot()
    
    if freeSpot == False:
        return True

    for num in range(0,10):
        if isSafe(freeSpot[0], freeSpot[1], num):
            sudokuTable[freeSpot[0]][freeSpot[1]] = num

            if solve() == True:
                return True

            sudokuTable[freeSpot[0]][freeSpot[1]] = 0

    return False

def getEmptySudokuTable():
    return [[0 for x in xrange(9)] for x in xrange(9)]

fSudokus = open("sudoku.txt", "r");
sudokuCollection = []
row = 0
numSudokus = 0
totalSum = 0

for idx, line in enumerate(fSudokus):
    if line.find("Grid") == 0:
        if idx == 0:
            row = 0
            sudoku = getEmptySudokuTable()
        else:
            sudokuCollection.insert(numSudokus, sudoku)
            sudoku = getEmptySudokuTable()
            row = 0
            numSudokus += 1
    else:
        for subidx, num in enumerate(line):
            if num.isdigit():
                sudoku[row][subidx] = int(num)
        row += 1

sudokuCollection.insert(numSudokus, sudoku)

fSudokus.close()

for index, sudoku in enumerate(sudokuCollection):
    print "Solving Sudoku #", index
    sudokuTable = sudoku
    solve()
    printTable(sudokuTable)
    print ""
    totalSum += int(str(sudokuTable[0][0])+str(sudokuTable[0][1])+str(sudokuTable[0][2]))

print totalSum



