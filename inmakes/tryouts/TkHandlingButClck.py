from tkinter import *
root=Tk()
def fun():
    print("Click here")
button1=Button(root,text="OK",command=fun)
button1.pack()
root.mainloop()