'''
    Sudoku is a logic-based, combinatorial number-placement puzzle.
    The objective is to fill a 9×9 grid with digits so that
    each column, each row, and each of the nine 3×3 subgrids that compose the grid
    contains all of the digits from 1 to 9.

    Complete the check_sudoku function to check if the given grid
    satisfies all the sudoku rules given in the statement above.
'''

def next_cell(grid,i,j):
    for val in range(i,9):
        for val in range(j,9):
            if grid[a][b] == 0:
                return a,b

    for val in range(0,9):
        for val in range(0,9):
            if grid[a][b] == 0:
    return -1 -1

def if_valid(grid,i,j,e):
    row = all([e != grid[i][x] for x in range(9)])
    if row:
        column = all([e != grid[x][j] for x in range(9)])
        if column:

def check_sudoku(sudoku):
    '''
        Your solution goes here. You may add other helper functions as needed.
        The function has to return True for a valid sudoku grid and false otherwise
'''

def main():
    '''
        main function to read input sudoku from console
        call check_sudoku function and print the result to console
    '''
    
    # initialize empty list
    sudoku = []

    # loop to read 9 lines of input from console
    for i in range(9):
        # read a line, split it on SPACE and append row to list
        row = input().split(' ')
        sudoku.append(row)
    # call solution function and print result to console
    print(check_sudoku(sudoku))

if __name__ == '__main__':
    main()
