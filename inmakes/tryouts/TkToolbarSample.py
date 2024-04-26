from tkinter import *
root=Tk()

mymenu=Menu(root)
root.config(menu=mymenu)
submenu=Menu(mymenu)

mymenu.add_cascade(label="File",menu=submenu)
submenu.add_command(label="save")

newmenu=Menu(mymenu)
mymenu.add_cascade(label="Edit",menu=newmenu)
newmenu.add_command(label="undo")

toolbar=Frame(root,bg="pink")
toolbar.pack(side=TOP,fill=X)
inbutton=Button(toolbar,text="Crop")
inbutton.pack()

root.mainloop()