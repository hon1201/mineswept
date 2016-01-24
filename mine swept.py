from tkinter import *
    
add_num(add_boom(new_game()))



layout = Tk()
layout.geometry('250x270+100+200')
layout.title('Mine sweeper')

for i in range(10):
    for j in range(10):
        button = Button(layout, text = ' ',command = print(mat[i][j]),height = 1, width = 2).grid(row = i ,column = j)
        in_game(mat)
        
layout.mainloop()  




                
                    


                
            
            
            
    
    
        
