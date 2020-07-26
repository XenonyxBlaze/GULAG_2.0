import sqlcon
from tkinter import *

root = Tk()
root.title("Gulag2.0 [Test]")

def connect(pwd):
    if sqlcon.con(pwd):
        outp = Label(root, text="Connected", padx=25,pady=20)
        outp.grid(row=3, columnspan=4)
        e.delete(0, END)
        e.insert(0, "Already connected")
    else:
        outp = Label(root, text="Wrong password", padx=25,pady=20)
        outp.grid(row=3, columnspan=4)
        print('Wrong password')
        root.quit()

wlcm = Label(root, text="Welcome to GULAG 2.0", padx = 30, pady = 10)
pwd = Label(root, text="Enter root password")
e = Entry(root)
e.grid(row=1, column = 0)

butn = Button(root, text="Connect", padx=10, command = lambda: connect(str(e.get())))

wlcm.grid(row=0,column=0,columnspan=2)
pwd.grid(row=1,column=0)
e.grid(row=1,column=1)
butn.grid(row=2,column=0)


root.mainloop()
