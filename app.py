import sqlcon
from tkinter import *
from PIL import ImageTk,Image

root = Tk()
root.iconbitmap("gulag.ico")
root.title("Gulag2.0 [Test]")


#Function Definitions
#----------------------------------------------------

def conect():
    if sqlcon.con(pswrd.get()):
        pswrd.grid_forget()
        con_btn.grid_forget()
        dispConStatus(True)
        con_status.grid(row=2, sticky=W+E, columnspan=3, pady=10)
    else:
        dispConStatus(False)
        con_status.grid(row=2, sticky=W+E, columnspan=3, pady=10)

def dispConStatus(bool):
    global con_status
    if bool:
        con_status = Label(root,text="Connected Successfully",fg="green", bd=2, relief=SUNKEN, anchor=W)
    else:
        con_status = Label(root,text="Error in connection",fg="red", bd=2, relief=SUNKEN, anchor=W)

#----------------------------------------------------



#GUI DEFINATIONS
#----------------------------------------------------

wlcm = Label(root, text="Welcome to GULAG 2.0 (testing ver.)")
logo_def = ImageTk.PhotoImage(Image.open("Gulag.png"))
logo = Label(image= logo_def)

pswrd = Entry(root)
pswrd.insert(0,"Enter password")

con_btn = Button(root, text="Connect", command=conect)

#----------------------------------------------------

#GUI grid display
#----------------------------------------------------

wlcm.grid(row=0,column=0)
logo.grid(row=0,column=1)
pswrd.grid(row=1,column=0,padx=10)
con_btn.grid(row=1,column=1)
#----------------------------------------------------

root.mainloop()
