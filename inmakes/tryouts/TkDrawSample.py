from tkinter import *
root=Tk()
canvas=Canvas(root,width=100,height=100)
canvas.pack()
newLine=canvas.create_line(0,0,8,90,fill="green")
newRect=canvas.create_rectangle(20,1,80,100,fill="red")

root.mainloop()