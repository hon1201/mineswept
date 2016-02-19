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
        self.state = True

    def becomebutton(self,i ,j,b,mat):
        self = Button(layout,command = lambda: show_value(i, j,b,mat), width = 2).grid(column = j, row = i)

    def over(self):
        self.state = False


def lose(b,mat):
    lose = Tk()
    lose.geometry('+150+300')
    label = Label(lose, text = 'You Lose').pack()
    for i in range(10):
        for j in range(10):
            if mat[i][j] == 9:
                b[i][j] = Button(layout, text = mat[i][j],state = DISABLED, width = 2).grid(column = j , row = i)

            elif mat[i][j] != 9:
                if b[i][j].state == True:
                    b[i][j] = Button(layout,state = DISABLED, width = 2).grid(column = j , row = i)

def win(mat, b):
    win = Tk()
    win.geometry('+150+300')
    label = Label(win, text = 'You Win').pack()
    for i in range(10):
        for j in range(10):
            if mat[i][j] == 9:
                b[i][j] = Button(layout, text = mat[i][j],state = DISABLED, width = 2).grid(column = j , row = i)
                
def show_value(i ,j,b,mat):
    count = 0 
    self = Button(layout, text = mat[i][j],state = DISABLED, width = 2).grid(column = j , row = i)
    b[i][j].over()
    if mat[i][j] == 9:
        lose(b, mat)

    else:
        for q in range(10):
            for w in range(10):
                if b[q][w].state == False:
                    count += 1

    if count == 90:
        win(mat, b)

for i in range(10):
  for j in range(10):
    b[i][j] = Box(mat[i][j])
    b[i][j].becomebutton(i, j,b,mat)




layout.mainloop()
    
