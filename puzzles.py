
# my email: miqdad.physics@gmail.com

#import random
import random as rad


# define a function to check for zeros
def there_zero(puzzle, hor_dim, ver_dim):
    for r in range(hor_dim):
        for c in range(ver_dim):
            if puzzle[r][c] == 0:
                return True
    # no zeros
    return False


# define a function to create the sudoku grid
def sudoku_generator(num_empty, hor_dim, ver_dim):
    # create the grid with zeros as place holder
    puzzle = [[0 for i in range(hor_dim)] for i in range(ver_dim)]
    # insert empty spaces as -1
    # pick a random position on the grid as empty
    pos_hor_list = [i for i in range(hor_dim)]
    pos_ver_list = [i for i in range(ver_dim)]
    while num_empty >= 0:
        # if it's available assign to it
        h = rad.choice(pos_hor_list)
        v = rad.choice(pos_ver_list)
        if puzzle[h][v] == 0:
            puzzle[h][v] = -1
        # decrement num_empty
        num_empty -= 1
    # loop until there is no zero
    while there_zero(puzzle, hor_dim, ver_dim):
        for r in range(hor_dim):
            for c in range(ver_dim):
                # pick a random number between 1 to 9
                pick_num = rad.choice([1, 2, 3, 4, 5, 6, 7, 8, 9])
                # insert numbers but check not in row or column
                if (pick_num in puzzle[r]) or (pick_num in [puzzle[i][c] for i in range(ver_dim)]):
                    pass
                else:
                    if puzzle[r][c] != -1:
                        puzzle[r][c] = pick_num
    return puzzle


# work perfectly for 9x9 grids may for other
#print(sudoku_generator(21, 9, 9))
