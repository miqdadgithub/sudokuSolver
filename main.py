# import needed module
from puzzles import sudoku_generator


def find_next_empty(puzzle):
    # define a function to find the next empty space
    # empty space = -1
    # return row, col tuple (or None, None) if there is None)
    for r in range(9):
        for c in range(9):
            if puzzle[r][c] == -1:
                return r, c
    return None, None


def is_valid(puzzle, guess, row, col):
    # figures out whether the guess is valid guess
    # returns True if is valid, False otherwise(follow sudoku rules)

    # row
    row_value = puzzle[row]
    if guess in row_value:
        return False

    # column
    col_value = [puzzle[i][col] for i in range(9)]
    if guess in col_value:
        return False

    # 9x9 matrix
    row_start = (row//3)*3
    col_start = (col//3)*3

    for r in range(row_start, row_start+3):
        for c in range(col_start, col_start+3):
            if puzzle[r][c] == guess:
                return False

    return True


def sudoku_solver(puzzle):
    # define a solve sudoku puzzle using back tracing
    # puzzle is a list of lists each list is a row of puzzle
    # return whether a solution exist
    # step1: where to start
    row, col = find_next_empty(puzzle)
    # step2: if there's nowhere left
    if row is None:
        return True
    # step3: if there a place make a guess 1 -> 9
    for guess in range(1, 10):
        # step4: check if valid, use a helper function
        if is_valid(puzzle, guess, row, col):
            # step5: commit the guess
            puzzle[row][col] = guess
            # step6: recursively call our function
            if sudoku_solver(puzzle):
                return True
        # step7: if not valid or if our guess
        # does not solve the puzzle the we need
        # to backtrack and try a new number
        puzzle[row][col] = -1  # rest the guess
    # step8: the puzzle is unsolvable
    return False


# let test it
if __name__ == '__main__':
    # puzzle = sudoku_generator(56, 9, 9)#fix it generate unsolvable grids
    puzzle = [
        [3, 9, -1,  -1, 5, -1,  -1, -1, -1],
        [-1, -1, -1,   2, -1, -1,  -1, -1, 5],
        [-1, -1, -1,  7, 1, 9,  -1, 8, -1],

        [-1, 5, -1,  -1, 6, 8,  -1, -1, -1],
        [2, -1, 6,  -1, -1, 3,  -1, -1, -1],
        [-1, -1, -1,  -1, -1, -1, -1, -1, 4],

        [5, -1, -1,  -1, -1, -1,  -1, -1, -1],
        [6, 7, -1,  1, -1, 5,  -1, 4, -1],
        [1, -1, 9,  -1, -1, -1,  2, -1, -1]
    ]
    print(sudoku_solver(puzzle))
    print(puzzle)
