# Constantes
LARGEUR = 7
HAUTEUR = 6

# Variables
user_toggle = True

# Fonctions


def grid_create():
    grid = []
    for i in range(LARGEUR):
        grid.append([])
        for _ in range(HAUTEUR):
            grid[i].append('.')
    return grid


def rules(grid, user, user_toggle):
    # rules for user_1 using 0 as pions
    if user_toggle == True:
        for user in grid[user]:
            for i in grid[user]:
                # rules for adding a pion
                if grid[user][-i:] == '.':
                    grid[user][-i:] = 0
                    break
                # rules if the colunm is full
                elif grid[user][0] != '.':
                    print(
                        'La colonne est complète, veuillez réessayer.')
                    user_toggle = True
                    input(grid, user_toggle)
    # rules for user_2 using 1 as pions
    elif user == False:
        for user in grid[user]:
            for i in grid[user]:
                # rules for adding a pion
                if grid[user][-i:] == '.':
                    grid[user][-i:] = 1
                    break
                # rules if the colunm is full
                elif grid[user][0] != '.':
                    print(
                        'La colonne est complète, veuillez réessayer.')
                    user_toggle = False
                    input(grid, user_toggle)
    # rules for a draw
    compteur = 0
    for i in range(LARGEUR):
        for j in range(1):
            if grid[i][j] == 0 or grid[i][j] == 1:
                compteur += 1
            if compteur == LARGEUR:
                print('Le puissance 4 est complet, la partie est nulle.')
                break
    # rules to check if there is a match vertically
    if user_toggle == True:
        for i in range(len(grid)):
            if grid[i].count(0) == 4:
                print('Partie Gagnée par user_1')
    if user_toggle == False:
        for i in range(len(grid)):
            if grid[i].count(0) == 4:
                print('Partie Gagnée par user_2')
    # rules to check if there is a match horizontally
    if user_toggle == True:
        compteur = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):

                if compteur == 4:
                    print('Partie Gagnée par user_2')
                    break
    if user_toggle == False:
        compteur = 0
        for i in range(len(grid)):
            # LOOP
            if compteur == 4:
                print('Partie Gagnée par user_2')
                break


def input(grid, user_toggle):
    if user_toggle == True:
        user_1 = int(
            input('Entrez le n° de la colonne souhaitée pour jouer : ')) - 1
        rules(grid, user_1, user_toggle)
    if user_toggle == False:
        user_2 = int(
            input('Entrez le n° de la colonne souhaitée pour jouer : ')) - 1
        rules(grid, user_2, user_toggle)


def display_grid(grid):
    for i in range(HAUTEUR):
        for j in range(LARGEUR):
            if j != LARGEUR - 1:
                print(grid[j][i], end=' ')
            else:
                print(grid[j][i], end='\n')


# Main


def main():
    grid = grid_create()
    display_grid(grid)
    input(grid, user_toggle)


if __name__ == '__main__':
    main()
