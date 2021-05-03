'''
Sudoko solver example...
backtracking // recursive method
'''
import re


def possible(row, column, number, suduko):
    '''Checks if guess is valid sulotion'''

    #check for conflic in row return False
    for i in range(9):
        if suduko[row][i] == number:
            return False

    #check for conflic in column, return false
    for i in range(9):
        if suduko[i][column] == number:
            return False
    #check for conlict in 3x3 mini square, return
    c0 = (column//3)*3
    r0 = (row//3)*3
    for i in range(3):
        for j in range(3):
            if suduko[r0+i][c0+j] == number:
                return False

    #number is a possible solution
    return True


def solve(sudouko):
    '''' quessing a number at free square in sudoku'''
    for y in range(9):
        for x in range(9):
            if sudouko[y][x] == 0:
                for n in range(1,10):
                    if possible(y,x,n, sudouko):
                        sudouko[y][x] = n
                        solve(sudouko)
                        sudouko[y][x] = 0
                return
    sudoku_print(sudouko)
    input('Finns det fler lösningar?')


def sudoku_print(s):
    ''' Funktion to print sudoku in terminal'''
    wall = '-----------------------------'
    for row in range(9):
        for col in range(9):
            if col == 3:
                print('| {} '.format(s[row][col]), end='')
            elif col == 6:
                print('| {} '.format(s[row][col]), end='')
            elif col == 0 and row == 3:
                print(wall)
                print(' {} '.format(s[row][col]), end='')
            elif col == 0 and row == 6:
                print(wall)
                print(' {} '.format(s[row][col]), end='')
            elif col == 8:
                print(' {} '.format(s[row][col]))
            else:
                print(' {} '.format(s[row][col]), end='')

def load_board():
    '''' funktion for user to load sudoku puzzle into solvev, empty space in sudoku = 0  '''
    s = []
    var = []
    print('OBS! Tomma fält skrivs som 0')
    for i in range(1,10):
        while True:
            var = input('Skriv alla siffor i rad {} '. format(i))
            var = re.findall('[0-9]', var)
            if len(var) == 9:
                var = [int(item) for item in var]
                s.append(var)
                break
            else:
                print('Fel antal siffror')
    return s

sudoko_puzzle = load_board()
solve(sudoko_puzzle)

