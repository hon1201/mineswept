from tkinter import *
from engine import *

     
mat = new_game()
add_boom(mat)
add_num(mat)

layout = Tk()
layout.geometry('250x270+100+200')
layout.title('Mine sweeper')

b = new_game()

class Box:

    def __init__(self, value):
        self.value = value
        self.status = True

    def becomebutton(self,i ,j,b,mat):
        self = Button(layout,command = lambda: show(i, j,b,mat), width = 2).grid(column = j, row = i)

    def over(self):
        self.status = False

    def show_value(self,i ,j,b,mat):
        count = 0
        self.over()
        self = Button(layout, text = mat[i][j],state = DISABLED, width = 2).grid(column = j , row = i)
##        if mat[i][j] == 0:
##            check(i , j ,b, mat)
        
        if mat[i][j] == 9:
            lose(b, mat)

        else:
            for q in range(10):
                for w in range(10):
                    if b[q][w].status == False:
                        count += 1

        if count == 90:
            win(mat, b)

def show(i, j, b, mat):
    b[i][j].show_value(i, j, b, mat)
    


def lose(b,mat):
    lose = Tk()
    lose.geometry('+150+300')
    label = Label(lose, text = 'You Lose').pack()
    for i in range(10):
        for j in range(10):
            if mat[i][j] == 9:
                b[i][j] = Button(layout, text = mat[i][j],state = DISABLED, width = 2).grid(column = j , row = i)

            elif mat[i][j] != 9:
                if b[i][j].status == True:
                    b[i][j] = Button(layout,state = DISABLED, width = 2).grid(column = j , row = i)

def win(mat, b):
    win = Tk()
    win.geometry('+150+300')
    label = Label(win, text = 'You Win').pack()
    for i in range(10):
        for j in range(10):
            if mat[i][j] == 9:
                b[i][j] = Button(layout, text = mat[i][j],state = DISABLED, width = 2).grid(column = j , row = i)
                
            
def check(i, j , b ,mat):
        if i == 0  and j == 0: 
            show(i, j+1, b, mat)
            show(i+1, j, b, mat)

        elif i == 0 and j == 9:
            show(i, j-1, b, mat)
            show(i+1, j, b, mat)

        elif i == 9 and j == 0:
            show(i-1, j , b, mat)
            show(i, j+1, b, mat)

        elif i == 9 and j == 9:
            show(i-1, j,b, mat)
            show(i, j+1, b, mat)

        elif i == 0 and (j != 0 or j != 9):
            show(i, j-1, b, mat)
            show(i, j+1, b, mat)
            show(i+1, j, b, mat)

        elif i == 9 and (j != 0 or j != 9):
            show(i-1, j, b, mat)
            show(i+1, j, b, mat)
            show(i , j-1, b, mat)

        elif j == 0 and (i != 0 or i != 9):
            show(i-1, j, b, mat)
            show(i+1, j, b, mat)
            show(i, j+1, b, mat)

        elif j == 9 and (i != 0 or i != 9):
            show(i, j-1, b, mat)
            show(i, j+1, b, mat)
            show(i-1, j, b, mat)

        else:
            show(i-1, j ,b, mat)
            show(i, j-1, b, mat)
            show(i, j+1, b, mat)
            show(i+1, j, b, mat)
                

##def show_value(i ,j,b,mat):
##    count = 0
##    self.over()
##    self = Button(layout, text = mat[i][j],state = DISABLED, width = 2).grid(column = j , row = i)
##    if mat[i][j] == 0:
##        check(i , j ,b, mat)
##    
##    if mat[i][j] == 9:
##        lose(b, mat)
##
##    else:
##        for q in range(10):
##            for w in range(10):
##                if b[q][w].status == False:
##                    count += 1
##
##    if count == 90:
##        win(mat, b)

for i in range(10):
  for j in range(10):
    b[i][j] = Box(mat[i][j])
    b[i][j].becomebutton(i, j,b,mat)




layout.mainloop()
    
