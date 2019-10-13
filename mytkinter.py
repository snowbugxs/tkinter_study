# -*- coding: utf-8 -*-
"""
Created on Fri Sep 27 19:29:26 2019

@author: local_admin
"""
import tkinter
 
window = tkinter.Tk()
window.title('my window')

## pack()  
#labela = tkinter.Label(window, text = "Suf. width", fg = "white", bg = "purple").pack() 
#labelb = tkinter.Label(window, text = "Taking all available X width", fg = "white", bg = "green").pack(fill = "x")  
#labelc = tkinter.Label(window, text = "Taking all available Y height", fg = "white", bg = "black").pack(side = "left", fill = "y")  
### grid()  
#tkinter.Label(window, text = 'Username').grid(row=0,column=1)
#tkinter.Entry(window).grid(row=0,column=1)
#tkinter.Entry(window).grid(row=1,column=1)
#tkinter.Checkbutton(window, text='keep me logged in').grid(columnspan=2)
### binding functions 
#def say_hi():
#    tkinter.Label(window, text='hi').pack()
#    
##tkinter.Button(window, text='click me', command=say_hi).pack() 
#btn = tkinter.Button(window, text = 'click')
#btn.bind('<Button-1>', say_hi)
#btn.pack() 
### events 
#def left_click(event):
#    tkinter.Label(window, text="left click").pack()
#def right_click(event):
#    tkinter.Label(window, text="right click").pack()
#def middle_click(event):
#    tkinter.Label(window, text="middle click").pack()
#    
#window.bind("<Button-1>", left_click)
#window.bind("<Button-2>", right_click)
#window.bind("<Button-3>", right_click)

## menu ## 
def function():
    pass 

root_menu = tkinter.Menu(window)
window.config(menu=root_menu)
file_menu = tkinter.Menu(root_menu)
root_menu.add_cascade(label='file', menu=file_menu)
file_menu.add_command(label='new file ...', command=function)
file_menu.add_separator()
file_menu.add_command(label='EXIT', command=window.quit) 
edit_menu = tkinter.Menu(root_menu)
root_menu.add_cascade(label='edit', menu=edit_menu)
edit_menu.add_command(label='undo', command=function)
edit_menu.add_command(label='redo', command=function)





#top_frame = tkinter.Frame(window).pack()
#bottom_frame = tkinter.Frame(window).pack(side = "bottom")
#btn1 = tkinter.Button(top_frame, text = "Button1", fg = "red").pack()
#btn2 = tkinter.Button(top_frame, text = "Button2", fg = "green").pack()
#btn3 = tkinter.Button(bottom_frame, text = "Button3", fg = "purple").pack(side = "left")
#btn4 = tkinter.Button(bottom_frame, text = "Button4", fg = "orange").pack(side = "left") 


 
window.mainloop()
