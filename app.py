'''

GULAG 2.0
GULAG 2.0 is a tkinter based GUI ver. of the original GulagPy with much more
functionality using MySQL.

Authors: Aarav Rajput, Dhruv Arora, Abheek Tripathi

Join The GULAG discord server : https://discord.gg/CE9CafD

'''
import sqlcon
from tkinter import  *
from tkinter import  ttk
from tkinter import  font
from tkinter import  messagebox
from PIL import ImageTk,Image










#Connection
#----------------------------------------------------------------------------------------------------------------------
def conWinCall():
    conCheckStatus = sqlcon.conect('000','000','000')
    connectionMenu.entryconfigure('Connect',state='disabled')

    conWin = Toplevel()
    conWin.title('Connection')
    conWin.iconbitmap('gulag.ico')
    conWin.resizable(False,False)

    conFrame=ttk.Frame(conWin,padding="3 3 12 0")
    conFrame.grid(row=0,column=0,padx=5,pady=5)
    
    Label(conFrame,text='Enter Host\t:').grid(row=0,column=0)
    conHost = Entry(conFrame)
    conHost.insert(0,'localhost')
    conHost.grid(row=0,column=1)

    Label(conFrame,text='Enter Username\t:').grid(row=1,column=0)
    conUsr = Entry(conFrame)
    conUsr.insert(0,'root')
    conUsr.focus()
    conUsr.grid(row=1,column=1)

    Label(conFrame,text='Enter Password\t:').grid(row=2,column=0)
    conPswrd = Entry(conFrame,show="*")
    conPswrd.grid(row=2,column=1)

    def conCheck():
        conCheckStatus = sqlcon.conect(conHost.get(),conUsr.get(),conPswrd.get())
        if conCheckStatus.con_bool:
            messagebox.showinfo("Connected","Successfully connected to "+conHost.get())
            conWin.destroy()
        else:
            messagebox.showerror("NotConnected","Error: \n"+conCheckStatus.con_err)
            conWin.destroy()


    Button(conFrame,text="Connect",command=conCheck,bg='green',fg='white').grid(row=3,column=1,columnspan=1,pady=10)

    root.wait_window(conWin)
    try:
        if conCheckStatus.con_bool:
            connectionMenu.entryconfigure('Connect',state='disabled',label='Connected to MySQL')
        else:
            connectionMenu.entryconfigure('Connect',state='normal')
    except:
        return
#----------------------------------------------------------------------------------------------------------------------










#Bug Report
#----------------------------------------------------------------------------------------------------------------------
def bugRepWinCall():
    feedbackMenu.entryconfigure('Report Bug',state='disabled')

    bugRepWin = Toplevel()
    bugRepWin.title('Report Bug')
    bugRepWin.iconbitmap('gulag.ico')
    bugRepWin.geometry('400x300')
    #bugRepWin.resizable(False,False)

    bugRepFrame = ttk.Frame(bugRepWin,padding="5 5 5 5")
    bugRepFrame.grid(row=0,column=0,pady=10)

    ttk.Label(bugRepFrame, text='Module Name\t:').grid(row=1,column=0,sticky=W+E)
    repMod = Entry(bugRepFrame,width=40)
    repMod.focus()
    repMod.grid(row=1,column=1,pady=5)

    ttk.Label(bugRepFrame, text='Report\t:').grid(row=2,column=0,sticky=N+E)
    repContent = Text(bugRepFrame,height=10,width=30,wrap='word')
    repContent.grid(row=2,column=1,pady=5,padx=10)

    repContentScroll = ttk.Scrollbar(bugRepFrame,orient=VERTICAL,command=repContent.yview)
    repContentScroll.grid(row=2,column=2,sticky=(N,S))

    repContent['yscrollcommand']=repContentScroll.set

    def repBug():
        bugRepWin.destroy()
        return

    Button(bugRepFrame,text='Submit',command=repBug).grid(row=3,column=1,pady=15)

    root.wait_window(bugRepWin)
    try:
        feedbackMenu.entryconfigure('Report Bug',state='normal')
    except:
        return
#----------------------------------------------------------------------------------------------------------------------










#Root Window
#----------------------------------------------------------------------------------------------------------------------
root = Tk()
root.iconbitmap('gulag.ico')
root.title('GULAG 2.0 (development)')
root.geometry('800x600')
root.minsize(width=800,height=600)
root.option_add('*tearOff',False)

content = ttk.Frame(root)
content.grid(sticky=(N,E,W,S))

Header = ttk.Frame(content,padding=(3,3,12,12),relief="groove")
Header.grid(row=0,column=0,sticky=(N,E,W,S),padx=5,pady=0)

headFont = font.Font(family="Helvetica",size=40,weight='bold')

logo = ImageTk.PhotoImage(file='Gulag.png')
ttk.Label(Header,image=logo).grid(row=0,column=0)
ttk.Label(Header,text="GULAG 2.0",font=headFont).grid(row=0,column=1,sticky=E)

Body = ttk.Frame(content,width=590,height=350,relief="groove")
Body.grid(row=1,column=0,padx=5,pady=2,sticky=(N,E,W,S))

panedWin1 =ttk.Panedwindow(Body, orient=HORIZONTAL)

dbFrame = ttk.Labelframe(panedWin1,text='Databases',width=100,height=100)
tbFrame = ttk.Labelframe(panedWin1,text='Tables',width=100,height=100)

panedWin1.add(dbFrame)
panedWin1.add(tbFrame)

panedWin1.grid(padx=5,pady=5)


'''Figuring out how to put tables on screen
ids = [302,456,278,349,221,107,445]
crimes = ['Murder','Hacking','Drug Trafficking','Robbery','Burglary','Assault on officer','Kidnapping']
pds=[60,25,40,5,3,2,10]
li=[]
for i in range(len(crimes)):
    li.append([crimes[i],ids[i],pds[i]])
nC = 0
for i in li:
    for j in i:
        nC += 1
    break
RecDisp = ttk.Frame(Body)
RecDisp.grid(padx=5,pady=5)
nR = 0
for i in li:
    nC = 0
    for j in i:
        Label(RecDisp, text=str(j)+"\t").grid(row=nR,column=nC)
        nC += 1
    nR += 1

'''
#----------------------------------------------------------------------------------------------------------------------









#Menubar Magic
#----------------------------------------------------------------------------------------------------------------------
menubarRoot = Menu(root,name='system')
connectionMenu = Menu(menubarRoot)
feedbackMenu = Menu(menubarRoot)
helpMenu = Menu(menubarRoot)
menubarRoot.add_cascade(menu=connectionMenu,label='Connection')
menubarRoot.add_cascade(menu=feedbackMenu, label='Feedback')
menubarRoot.add_cascade(menu=helpMenu, label='Help')

connectionMenu.add_command(label='Connect',command=conWinCall)

feedbackMenu.add_command(label='Report Bug',command=bugRepWinCall)
feedbackMenu.add_command(label='Provide Feedback')

helpMenu.add_command(label='How To Use')
helpMenu.add_command(label='Redownload Database')
helpMenu.add_separator()
helpMenu.add_command(label='Developer Contact')

root['menu']=menubarRoot
#----------------------------------------------------------------------------------------------------------------------









#Window Resizing Magic
#----------------------------------------------------------------------------------------------------------------------
root.columnconfigure(0, weight=1,minsize=600)
root.rowconfigure(0, weight=1,minsize=600)
content.columnconfigure(0, weight=1)
content.rowconfigure(0, weight=0)
content.rowconfigure(1, weight=3)
#----------------------------------------------------------------------------------------------------------------------

root.mainloop()
