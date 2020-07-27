import sqlcon
from tkinter import *
from PIL import ImageTk,Image

root = Tk()
root.iconbitmap("gulag.ico")
root.title("Gulag2.0 [Test]")


#Function Definitions
#----------------------------------------------------

def conect():
    global conStatusClass
    conStatusClass = sqlcon.con(pswrd.get())
    if conStatusClass.con_bool:
        connectFrame.grid_forget()
        dispConStatus(True)
    else:
        dispConStatus(False)
    con_status.grid(row=2, sticky=W+E, columnspan=3, pady=10)

def dispConStatus(bool):
    global con_status
    if bool:
        con_status = Label(root,text="Connected Successfully",fg="green", bd=2, relief=SUNKEN, anchor=W)
    else:
        con_status = Label(root,text="Error in connection: "+conStatusClass.con_err,fg="red", bd=2, relief=SUNKEN, anchor=W)

#----------------------------------------------------



#GUI DEFINATIONS
#----------------------------------------------------

wlcm = Label(root, text="Welcome to GULAG 2.0 (testing ver.)")
logo_def = ImageTk.PhotoImage(Image.open("Gulag.png"))
logo = Label(image= logo_def)

connectFrame = LabelFrame(root, text="Enter password",padx=10,pady=10)

pswrd = Entry(connectFrame)


con_btn = Button(connectFrame, text="Connect", command=conect)

#----------------------------------------------------

#GUI grid display
#----------------------------------------------------

wlcm.grid(row=0,column=0)
logo.grid(row=0,column=1)

connectFrame.grid(row=1,columnspan=2,sticky=W+E,padx=10,pady=5)

pswrd.grid(row=0,column=0,padx=10)
con_btn.grid(row=0,column=1)
#----------------------------------------------------

root.mainloop()
