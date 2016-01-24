from tkinter import *

layout = Tk()
layout.geometry('250x270+100+200')
layout.title('Mine sweeper')

for i in range(10):
    for j in range(10):
        button = Button(layout, text = ' ',height = 1, width = 2).grid( row= i, column = j   )   


layout.mainloop()  

