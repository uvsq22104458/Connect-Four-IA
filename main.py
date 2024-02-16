###############
# Importation #
###############
import sys as s
############
# Constant #
############
LARGEUR = 7
HAUTEUR = 6
#############
# Variables #
#############
user_toggle = True
#############
# Functions #
#############


def grid_create():
    # Create a grid full of '.'.
    grid = []
    for i in range(LARGEUR):
        grid.append([])
        for _ in range(HAUTEUR):
            grid[i].append('.')
    return grid


def rules(grid, user, user_toggle):
    # Rules for adding a pawn, verify if the column if full or if it's a draw.
    # Check if there is any horizontally, vertically or diagonally match.
    # Switch to the next user after the first user played.
    compteur_0 = 0
    compteur_1 = 0
    # Add a pawn.
    for i in range(1, LARGEUR + 1):
        if grid[user][-i] == '.':
            if user_toggle == True:
                grid[user][-i] = 0
                break
            else:
                grid[user][-i] = 1
                break
    # Check if the colunm is full.
        elif grid[user][0] != '.':
            print(
                'La colonne est complète, veuillez réessayer.')
            input_user(grid, user_toggle)
    # Check for a draw
    for i in range(LARGEUR):
        if grid[i][0] == 0 or grid[i][0] == 1:
            compteur_0 += 1
        if compteur_0 == LARGEUR:
            print('Le puissance 4 est complet, la partie est nulle.')
            compteur_0 = 0
            exit_program(grid)
    # Check if there is a match vertically.
    for i in range(LARGEUR):
        for j in range(HAUTEUR):
            if grid[i][j] == 0:
                compteur_0 += 1
            elif grid[i][j] == 1:
                compteur_1 += 1
            elif compteur_1 == 4 or compteur_0 == 4:
                compteur_1 = 0
                compteur_0 = 0
                exit_program(grid)
            else:
                compteur_1 = 0
                compteur_0 = 0
    # Check if there is a match horizontally.
    for i in range(HAUTEUR):
        for j in range(LARGEUR):
            if grid[j][i] == 0:
                compteur_0 += 1
            elif grid[j][i] == 1:
                compteur_1 += 1
            elif compteur_1 == 4 or compteur_0 == 4:
                compteur_1 = 0
                compteur_0 = 0
                exit_program(grid)
            else:
                compteur_1 = 0
                compteur_0 = 0
    # Check if there is a match diagonally.
    for i in range(LARGEUR):
        for j in range(HAUTEUR):
            if grid[i:i+3][j:j+3] == [0, 0, 0, 0] or grid[i:i+3][j:j+3] == [1, 1, 1, 1] or grid[i:i+3][j:j-3] == [0, 0, 0, 0] or grid[i:i+3][j:j-3] == [1, 1, 1, 1]:
                exit_program(grid)
    # Switching to the other user if the first user played.
    if user_toggle == False:
        user_toggle = True
        input_user(grid, user_toggle)
    if user_toggle == True:
        user_toggle = False
        input_user(grid, user_toggle)


def input_user(grid, user_toggle):
    # Check if the turn is for user_0 or user_1.
    # user_0 start first.
    if user_toggle == True:
        display_grid(grid)
        user_0 = int(
            input('User_0 le n° de la colonne souhaitée pour jouer : ')) - 1
        rules(grid, user_0, user_toggle)
    if user_toggle == False:
        display_grid(grid)
        user_1 = int(
            input('User_1 le n° de la colonne souhaitée pour jouer : ')) - 1
        rules(grid, user_1, user_toggle)


def display_grid(grid):
    # Display each list of the grid vertically to form a real connect-four
    for i in range(HAUTEUR):
        for j in range(LARGEUR):
            if j != HAUTEUR:
                print(grid[j][i], end=' ')
            else:
                print(grid[j][i], end='\n')


def exit_program(grid):
    # Exit the program when the game is over using exit() function.
    display_grid(grid)
    print('Partie Terminée')
    print('Exiting the program...')
    s.exit(0)

########
# Main #
########


def main():
    # Main function where the interpreter start it first.
    grid = grid_create()
    input_user(grid, user_toggle)


if __name__ == '__main__':
    main()
