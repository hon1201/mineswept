from random import randint
from tkinter import *




 
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
                    if mat[0][1] == 9  and mat[1][0] == 9 and mat[1][1] == 9:
                        mat [0][0] += 3

                    elif mat[0][1] == 9 and (mat[1][0] or mat[1][1]) == 9:
                        mat[0][0] += 2

                    elif mat[1][0] == 9 and mat[1][1] == 9 :
                        mat[0][0] += 2

                    elif mat[0][1] == 9 or mat[1][0] == 9 or mat[1][1] == 9:
                        mat[0][0] += 1
     
                elif i == 0  and j == 9 :
                    if mat[0][8] == 9  and mat[1][9] == 9 and mat[1][8] == 9:
                        mat [0][9] += 3

                    elif mat[0][8] == 9 and (mat[1][9] or mat[1][8] == 9):
                        mat[0][9] += 2

                    elif mat[1][9] == 9 and mat [1][8] == 9 :
                        mat[0][9] += 2

                    elif mat[0][8] == 9 or mat[1][9] == 9 or mat[1][8] == 9:
                        mat[0][9] += 1
                    
                elif i == 9 and j == 0 :
                    if mat[8][0] == 9  and mat[9][1] == 9 and mat[8][1] == 9:
                        mat [9][0] += 3

                    elif mat[8][0] == 9 and (mat[9][1] or mat[8][1] == 9):
                        mat[9][0] += 2

                    elif mat[9][1] == 9 and mat [8][1] == 9 :
                        mat[9][0] += 2

                    elif mat[8][0] == 9 or mat[9][1] == 9 or mat[8][1] == 9:
                        mat[9][0] += 1

                elif i == 9 and j == 9:
                    if mat[9][8] == 9  and mat[8][9] == 9 and mat[8][8] == 9:
                        mat [9][9] += 3

                    elif mat[9][8] == 9 and (mat[8][9] or mat[8][8] == 9):
                        mat[9][9] += 2

                    elif mat[8][9] == 9 and mat [8][8] == 9 :
                        mat[9][9] += 2

                    elif mat[9][8] == 9 or mat[8][9] == 9 or mat[8][8] == 9:
                        mat[9][9] += 1


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
    while True:
##        print(pmat)
        rate = 0 
##        position(input('row: '), input('column: '), input('press b to place a flat: '), mat , pmat)
        for i in range(10):
            if 9 in pmat[i]:
##                print(pmat)
                return ('You Lose')

            else:
                continue
        for a in range(10):
            for b in range(10):
                if mat[a][b] == 9 and pmat[a][b] == '*':
                    rate += 1

                else :
                    continue

##        print(rate)
        if rate == 10:
            return ('You Win')  
                    

    
add_num(add_boom(new_game()))



layout = Tk()
layout.geometry('250x270+100+200')
layout.title('Mine sweeper')

for i in range(10):
    for j in range(10):
        button = Button(layout, text = ' ',command = print(mat[i][j]),height = 1, width = 2).grid(row = i ,column = j)
        in_game(mat)
        
layout.mainloop()  




                
                    


                
            
            
            
    
    
        
