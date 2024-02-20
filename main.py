import sys as s
COLUMNS = 7
ROWS = 6
WIN_PATTERN_1 = [1, 1, 1, 1]
WIN_PATTERN_2 = [2, 2, 2, 2]
space = 0
colors = ["\033[0m", "\033[0;31m", "\033[1;33m"]
current_player = 1


def create_grid():

    global grid
    grid = []
    for column in range(COLUMNS):
        grid.append([])
        for _ in range(ROWS):
            grid[column].append(space)
    return grid


def display_grid():

    for row in range(ROWS):
        for column in range(COLUMNS):
            print(
                f"{colors[grid[column][row]]}.{colors[space]}", end="  ")
        print(end='\n')


def input_player():

    display_grid()
    try:
        column = int(
            input(f"{colors[current_player]}Player {current_player}{colors[space]}, choose a column to play (1-{COLUMNS}) :")) - 1
        if 0 <= column < COLUMNS:
            add_pawn(column)
        else:
            raise ValueError
    except ValueError:
        print(f'Error of value: try again.')
        input_player()


def add_pawn(column):

    for elem in range(ROWS-1, -1, -1):
        if grid[column][elem] == space:
            grid[column][elem] = current_player
            x, y = column, elem
            break
        elif grid[column][0] != space:
            print("La colonne est complète, veuillez réessayer.")
            input_player(grid, current_player)
    vertical_pattern = [grid[x][row] for row in range(ROWS)]
    alignments(vertical_pattern)
    horizontal_pattern = [grid[column][y] for column in range(COLUMNS)]
    alignments(horizontal_pattern)
    draw()
    toggle_player()


def alignments(pattern):
    for elem in range(len(pattern)):
        if pattern[elem:elem+len(WIN_PATTERN_1)] == WIN_PATTERN_1 or pattern[elem:elem+len(WIN_PATTERN_2)] == WIN_PATTERN_2:
            exit_program()


def draw():

    first_row = [column[0] for column in grid]
    if space not in first_row:
        print("Le puissance 4 est complet, la partie est nulle.")
        exit_program()


def toggle_player():

    global current_player
    current_player = (WIN_PATTERN_1[0]+WIN_PATTERN_2[0]) - current_player
    input_player()


def exit_program():

    display_grid()
    print(f"Player {current_player} has won.\nExiting the program...")
    s.exit(0)


def main():

    create_grid()
    input_player()


if __name__ == "__main__":
    main()
