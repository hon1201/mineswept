from tkinter import *
from engine import *

     
mat = new_game()
add_boom(mat)
add_num(mat)


layout = Tk()
layout.geometry('250x270+100+200')
layout.title('Mine sweeper')

##def display(i , j , mat,b):
##    print(i, j)
##    b[i][j] = Button(layout, text = mat[i][j] ,width = 2 ).grid(column = j , row = i)
##    print(b)
##  

b = new_game()
##
##print(b)
##
##for i in range(10):
##    for j in range(10):
####        b[i][j] = Button(layout, width = 2 ,command = lambda: display(i, j ,mat,b)).grid(column = j , row = i)
##      b[i][j] = Box(mat[i][j])
##        
##print(b[0][0].show_value())

def show_value(i ,j):
    self = Button(layout, text = mat[i][j], width = 2).grid(column = j , row = i)

class Box:

    def __init__(self, value):
        self.value = value

    def becomebutton(self,i ,j):
        self = Button(layout, command = lambda:show_value(i, j), width = 2).grid(column = j, row = i)




for i in range(10):
  for j in range(10):
    b[i][j] = Box(mat[i][j])
    b[i][j].becomebutton(i, j)



layout.mainloop()  

    
