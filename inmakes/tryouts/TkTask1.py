#make a GUI contains your Name and OK button
from tkinter import *
root=Tk()
Label(root,text="I'm Muzammil").pack()
button=Button(root,text="OK")
button.pack()
root.mainloop()