from tkinter import *
root=Tk()
l1=Label(root,text="username")
l2=Label(root,text="password")
entry1=Entry(root)
entry2=Entry(root)

l1.grid(row=0,column=0)
entry1.grid(row=0,column=1)
l2.grid(row=1,column=0)
entry2.grid(row=1,column=1)
root.mainloop()