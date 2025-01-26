# HTB Sudoking YS4B

NUM_LINES = 13
N = 9

def readLines():
    lines = []

    for _ in range(NUM_LINES):
        line = input()
        lines.append(line)

    return lines

def createMatrix(lines):
    matrix = []
    for line in lines:
        row = []
        for character in line:
            if character in "123456789":
                row.append(int(character))
            
            elif character == '.':
                row.append(0)
        if len(row) != 0:
            matrix.append(row)
    return matrix

def createLines(matrix):
    lines = "+-------+-------+-------+\n"
    
    for i in range(3):
        lines += f"| {matrix[i][0]} {matrix[i][1]} {matrix[i][2]} | {matrix[i][3]} {matrix[i][4]} {matrix[i][5]} | {matrix[i][6]} {matrix[i][7]} {matrix[i][8]} | \n"
    lines += "+-------+-------+-------+\n"
    for i in range(3,6):
        lines += f"| {matrix[i][0]} {matrix[i][1]} {matrix[i][2]} | {matrix[i][3]} {matrix[i][4]} {matrix[i][5]} | {matrix[i][6]} {matrix[i][7]} {matrix[i][8]} | \n"
    lines += "+-------+-------+-------+\n"
    for i in range(6,9):
        lines += f"| {matrix[i][0]} {matrix[i][1]} {matrix[i][2]} | {matrix[i][3]} {matrix[i][4]} {matrix[i][5]} | {matrix[i][6]} {matrix[i][7]} {matrix[i][8]} | \n"
    lines += "+-------+-------+-------+\n"
    
    return lines

#https://www.geeksforgeeks.org/sudoku-backtracking-7/

def isSafe(grid, row, col, num):
  
    # Check if we find the same num
    # in the similar row , we
    # return false
    for x in range(9):
        if grid[row][x] == num:
            return False

    # Check if we find the same num in
    # the similar column , we
    # return false
    for x in range(9):
        if grid[x][col] == num:
            return False

    # Check if we find the same num in
    # the particular 3*3 matrix,
    # we return false
    startRow = row - row % 3
    startCol = col - col % 3
    for i in range(3):
        for j in range(3):
            if grid[i + startRow][j + startCol] == num:
                return False
    return True

def solveSudoku(grid, row, col):
  
    # Check if we have reached the 8th
    # row and 9th column (0
    # indexed matrix) , we are
    # returning true to avoid
    # further backtracking
    if (row == N - 1 and col == N):
        return True
      
    # Check if column value  becomes 9 ,
    # we move to next row and
    # column start from 0
    if col == N:
        row += 1
        col = 0

    # Check if the current position of
    # the grid already contains
    # value >0, we iterate for next column
    if grid[row][col] > 0:
        return solveSudoku(grid, row, col + 1)
    for num in range(1, N + 1, 1):
      
        # Check if it is safe to place
        # the num (1-9)  in the
        # given row ,col  ->we
        # move to next column
        if isSafe(grid, row, col, num):
          
            # Assigning the num in
            # the current (row,col)
            # position of the grid
            # and assuming our assigned
            # num in the position
            # is correct
            grid[row][col] = num

            # Checking for next possibility with next
            # column
            if solveSudoku(grid, row, col + 1):
                return True

        # Removing the assigned num ,
        # since our assumption
        # was wrong , and we go for
        # next assumption with
        # diff num value
        grid[row][col] = 0
    return False



lines = readLines()

grid = createMatrix(lines)

solveSudoku(grid, 0, 0)

result = createLines(grid)

print(result) 
