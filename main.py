# Constantes
LARGEUR = 7
HAUTEUR = 6

# Fonctions


def grid_create():
    grid = []
    for i in range(LARGEUR):
        grid.append([])
        for _ in range(HAUTEUR):
            grid[i].append('.')
    return grid


def rules():


def input():
    user_1 = int(
        input('Entrez le n° de colonne où vous souhaitez mettre votre pion : '))
    rules()
    user_2 = int(
        input('Entrez le n° de colonne où vous souhaitez mettre votre pion : '))


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


if __name__ == '__main__':
    main()
