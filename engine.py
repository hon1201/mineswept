from random import randint



def new_game():
    size = 10*[0]
    mat = []
    for i in range (10):
        mat1 = [size.copy()]
        mat += mat1

    return mat

def add_boom(mat):
    for i in range (10):
        random = randint(0, 9)
        random1 = randint(0,9)
        mat[random][random1] = 9
        
    return mat

def add_num(mat):
    for i in range (10):
        for j in range(10):
            if mat[i][j] == 9:
                 continue
            else:
                if i == 0 and j == 0:
                    for q in range(2):
                        for w in range(2):
                            if q == 0 and w == 0 :
                                continue

                            elif mat[i+w][j+q] == 9 :
                                mat[i][j] += 1

     
                elif i == 0  and j == 9 :
                    for q in range(2):
                        for w in range(2):
                            if q == 1 and w == 0:
                                continue

                            elif mat[i+q][j-1+w] == 9 :
                                mat[i][j] += 1

                    
                elif i == 9 and j == 0 :
                    for q in range(2):
                        for w in range(2):
                            if q == 1 and w == 0:
                                continue

                            elif mat[i-1+q][j+w] == 9:
                                mat[i][j] += 1

                elif i == 9 and j == 9:
                    for q in range(2):
                        for w in range(2):
                            if q == 1 and w == 1:
                                continue

                            elif mat[i-1+w][j-1+q] == 9 :
                                mat[i][j] += 1


                elif i == 0 and (j != 0 or j != 9):
                    for q in range(2):
                        for w in range(3):
                            if q == 0 and w == 1:
                                continue

                            else:
                                if mat[i+q][j-1+w] == 9:
                                    mat[i][j] += 1

                elif i == 9 and (j != 0 or j != 9):
                    for q in range(2):
                        for w in range(3):
                            if q == 1 and w == 1:
                                continue

                            else:
                                if mat[i-1+q][j-1+w] == 9 :
                                    mat[i][j] += 1


                elif j == 0 and (i != 0  or i != 9):
                    for q in range(3):
                        for w in range(2):
                            if q == 0 and w == 1:
                                continue

                            else:
                                if mat[i-1+q][j+w] == 9 :
                                    mat[i][j] +=1

                elif j == 9 and (i != 0 or i != 9):
                    for q in range(3):
                        for w in range(2):
                            if q == 1 and w == 1:
                                continue

                            else:
                                if mat[i-1+q][j-1+w] == 9:
                                    mat[i][j] += 1
                else:
                    for a in range(3):
                        for b in range(3):
                            if a == 1 and b == 1:
                                continue

                            else:
                                if mat[i-1+b][j-1+a] == 9:
                                    mat[i][j] += 1

    return mat

def position(x, y, boom, mat, pmat):
    if boom  == 'b':
        pmat[int(x)][int(y)] = '*'
    else:
        pmat[int(x)][int(y)] = mat[int(x)][int(y)]

    return pmat
    
def in_game(mat):
    pmat = new_game()
    def print_game(pmat):
        for row in pmat:
            print(''.join(map(lambda x: str(x).rjust(5), row)))
    GRID_SIZE = 10
    while True:
        print_game(pmat)
        rate = 0 
        position(input('row: '), input('column: '), input('press b to place a flat: '), mat , pmat)
        
        for i in range(10):
            if 9 in pmat[i]:
                print_game(pmat)
                return ('You Lose')

            else:
                continue
        for a in range(10):
            for b in range(10):
                if mat[a][b] == 9 and pmat[a][b] == '*':
                    rate += 1

                else :
                    continue

        if rate == 10:
            return ('You Win')  



