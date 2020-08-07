'''

GULAG 2.0
GULAG 2.0 is a tkinter based GUI ver. of the original GulagPy with much more
functionality using MySQL.

Authors: Aarav Rajput, Dhruv Arora, Abheek Tripathi

Join The GULAG discord server for programming related doubt solving : https://discord.gg/CE9CafD
Website: https://gulag.heliohost.org

Gulag 2.0 is completely open-source and the code can be used in any way :)

'''
import sqlcon
from tkinter import  *
from tkinter import  ttk
from tkinter import  font
from tkinter import  messagebox
from PIL import ImageTk,Image










#Connection Window
#----------------------------------------------------------------------------------------------------------------------
def conWinCall():
    conCheckStatus = sqlcon.connectSQL('000','000','000')
    connectionMenu.entryconfigure('Connect',state='disabled')

    conWin = Toplevel()
    conWin.title('Connection')
    conWin.iconbitmap('gulag.ico')
    conWin.resizable(False,False)

    conFrame=ttk.Frame(conWin,padding="3 3 3 3")
    conFrame.grid(row=0,column=0,padx=5,pady=5)
    
    Label(conFrame,text='Enter Host\t:').grid(row=0,column=0)
    conHost = Entry(conFrame)
    conHost.insert(0,'65.19.141.67')
    conHost.grid(row=0,column=1)

    Label(conFrame,text='Enter Username\t:').grid(row=1,column=0)
    conUsr = Entry(conFrame)
    conUsr.insert(0,'gulag_root')
    conUsr.focus()
    conUsr.grid(row=1,column=1)

    Label(conFrame,text='Enter Password\t:').grid(row=2,column=0)
    conPswrd = Entry(conFrame,show="*")
    conPswrd.grid(row=2,column=1)

    def conCheck(*args):
        conCheckStatus = sqlcon.connectSQL(conHost.get(),conUsr.get(),conPswrd.get())
        if conCheckStatus.tf:
            messagebox.showinfo("Connected","Successfully connected to "+conHost.get())
            conWin.destroy()
        else:
            messagebox.showerror("NotConnected","Error: \n"+conCheckStatus.Msg)
            conWin.destroy()

    conPswrd.bind('<Return>',conCheck)


    ttk.Button(conFrame,style='greenButtons.TButton',text="Connect",command=conCheck).grid(row=3,column=1,columnspan=1,pady=10)

    root.wait_window(conWin)
    try:
        if conCheckStatus.tf:
            connectionMenu.entryconfigure('Connect',state='disabled',label='Connected to MySQL')
            updateDbBox()
        else:
            connectionMenu.entryconfigure('Connect',state='normal')
    except:
        return
#----------------------------------------------------------------------------------------------------------------------










#Bug Report Window
#----------------------------------------------------------------------------------------------------------------------
def bugRepWinCall():
    feedbackMenu.entryconfigure('Report Bug',state='disabled')

    bugRepWin = Toplevel()
    bugRepWin.title('Report Bug')
    bugRepWin.iconbitmap('gulag.ico')
    bugRepWin.geometry('400x300')
    bugRepWin.resizable(False,False)

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









#Feedback Window
#----------------------------------------------------------------------------------------------------------------------
def feedWinCall():
    feedbackMenu.entryconfigure('Provide Feedback',state='disabled')

    feedWin = Toplevel()
    feedWin.title('Feedback')
    feedWin.iconbitmap('gulag.ico')
    feedWin.geometry('400x300')
    feedWin.resizable(False,False)

    feedFrame = ttk.Frame(feedWin,padding="5 5 5 5")
    feedFrame.grid(row=0,column=0,pady=10)

    ttk.Label(feedFrame, text='Your Name\t:').grid(row=1,column=0,sticky=W+E)
    usrName = Entry(feedFrame,width=40)
    usrName.focus()
    usrName.grid(row=1,column=1,pady=5)

    ttk.Label(feedFrame, text='E-mail address\t:').grid(row=2,column=0,sticky=W+E)
    usrMail = Entry(feedFrame,width=40)
    usrMail.grid(row=2,column=1,pady=5)

    ttk.Label(feedFrame, text='Suggestions\t:').grid(row=9,column=0,sticky=N+E)
    feedSuggest = Text(feedFrame,height=5,width=30,wrap='word')
    feedSuggest.grid(row=9,column=1,pady=5,padx=10)

    feedSuggestScroll = ttk.Scrollbar(feedFrame,orient=VERTICAL,command=feedSuggest.yview)
    feedSuggestScroll.grid(row=9,column=2,sticky=(N,S))

    feedSuggest['yscrollcommand']=feedSuggestScroll.set

    def sendFeed():
        feedWin.destroy()
        return

    Button(feedFrame,text='Submit',command=sendFeed).grid(row=10,column=1,pady=15)

    root.wait_window(feedWin)
    try:
        feedbackMenu.entryconfigure('Provide Feedback',state='normal')
    except:
        return
#----------------------------------------------------------------------------------------------------------------------










#Functions
#----------------------------------------------------------------------------------------------------------------------


def updateDbBox():
    clearDB()
    dbListVar = sqlcon.returnDbList()
    for i in dbListVar:
        db_listbox.insert('end',i)
    db_listbox.selection_set(1)
    db_listbox.curselection(db_listbox.get(0,END).index('gulag_db'))
    updateTbBox()

def clearDB(*args):
    dbListVar = db_listbox.get(0,END)
    for i in dbListVar:
        db_listbox.delete(db_listbox.get(0,END).index(i))

def clearTB(*args):
    tbListVar = tb_listbox.get(0,END)
    for i in tbListVar:
        tb_listbox.delete(tb_listbox.get(0,END).index(i))
        
def updateTbBox(*args):
    x=sqlcon.use(db_listbox.get(db_listbox.curselection()))
    messagebox.showinfo("",x)
    clearTB()
    tbListVar = sqlcon.returnTbList()
    for i in tbListVar:
        tb_listbox.insert('end',i)

def clearTBD(*args):
    tbdListVar = tbd_listbox.get(0,END)
    for i in tbdListVar:
        tbd_listbox.delete(tbd_listbox.get(0,END).index(i))
        
def updateTbdBox(*args):
    x=sqlcon.returnTbdList(tb_listbox.get(tb_listbox.curselection())[0])
    clearTBD()
    tbdListVar = x
    for i in tbdListVar:
        tbd_listbox.insert('end',i)


def createMainApp(*args):
    return

#----------------------------------------------------------------------------------------------------------------------









#Root Window
#----------------------------------------------------------------------------------------------------------------------
root = Tk()
root.iconbitmap('gulag.ico')
root.title('GULAG 2.0 (development)')
root.geometry('800x600')
root.minsize(width=800,height=600)










#Styles Handling
#----------------------------------------------------------------------------------------------------------------------
styleHandle = ttk.Style()
styleHandle.configure('greenButtons.TButton',background='green',foreground='green')
#styleHandle.configure('redButtons.TButton',background='red',foreground='white')
headFont = font.Font(family="Arial Black",size=40)
bigFont = font.Font(family='Comic Sans MS',size=20,weight='bold')
styleHandle.configure('bigg.TLabel',foreground='#4a4d4f',font=bigFont)
styleHandle.configure('dark.TFrame',background='#4a4d4f',foreground='#a9aaab')
styleHandle.configure('dark.TLabel',background='#4a4d4f',foreground='#a9aaab',font=headFont)
styleHandle.configure('light.TFrame',background='#a9aaab',foreground='#4a4d4f')
#----------------------------------------------------------------------------------------------------------------------










content = ttk.Frame(root,style='dark.TFrame')
content.grid(sticky=(N,E,W,S))

Header = ttk.Frame(content,padding=(5,5,5,5),style='dark.TFrame')
Header.grid(row=0,column=0,sticky=(N,E,W,S),padx=5,pady=0)

logo = ImageTk.PhotoImage(Image.open('Gulag.png'))
ttk.Label(Header,image=logo,style='dark.TLabel').grid(row=0,column=0,sticky=W)
ttk.Label(Header,text="GULAG 2.0",style='dark.TLabel').grid(row=0,column=1,sticky=E)

Body = ttk.Frame(content,width=590,height=350,style='light.TFrame')
Body.grid(row=1,column=0,padx=5,pady=2,sticky=(N,E,W,S))

top_pane = ttk.Frame(Body)
top_pane.grid(row=0,column=0,columnspan=2,sticky=(N,E,W,S))

db_frame = ttk.Labelframe(top_pane, text='Databases',padding='3 3 3 3')
db_frame.grid(row=0,column=0,sticky=(S,W,E,N),padx=5)
db_listbox = Listbox(db_frame,height=5,width=30)
db_listbox.grid(row=0,column=0,sticky=(W))
dbScroller = ttk.Scrollbar(db_frame,orient=VERTICAL,command=db_listbox.yview)
dbScroller.grid(row=0,column=1,sticky=(N,S,W))
db_listbox['yscrollcommand']=dbScroller.set
db_listbox.bind('<Double-1>', updateTbBox)
db_listbox.bind('<Return>', updateTbBox)
db_console = ttk.Frame(db_frame)
db_console.grid(row=0,column=2,sticky=(N,E,W,S))

tb_frame = ttk.Labelframe(top_pane, text='Tables',padding='3 3 3 3')
tb_frame.grid(row=0,column=1,sticky=(S,W,E,N),padx=5)
tb_listbox = Listbox(tb_frame,height=5,width=30)
tb_listbox.grid(row=0,column=0,sticky=(W))
tbScroller = ttk.Scrollbar(tb_frame,orient=VERTICAL,command=tb_listbox.yview)
tbScroller.grid(row=0,column=1,sticky=(N,S,W))
tb_listbox['yscrollcommand']=tbScroller.set
tb_listbox.bind('<Double-1>', createMainApp)
tb_console = ttk.Frame(tb_frame)
tb_console.grid(row=0,column=2,sticky=(N,E,W,S))

info_frame = ttk.Frame(top_pane,relief='ridge')
info_frame.grid(row=0,column=2,padx=5)
ttk.Label(info_frame,text='Important',style='bigg.TLabel').grid(row=0,column=1,padx=5,pady=5)
ttk.Label(info_frame,text='Check out the documentation in the help menu \nto learn how to use before continuing',justify=CENTER).grid(row=1,columnspan=2,column=0,padx=5,pady=5)
#----------------------------------------------------------------------------------------------------------------------









#Menubar Magic
#----------------------------------------------------------------------------------------------------------------------
root.option_add('*tearOff',False)
menubarRoot = Menu(root)

connectionMenu = Menu(menubarRoot)
feedbackMenu = Menu(menubarRoot)
helpMenu = Menu(menubarRoot)

menubarRoot.add_cascade(menu=connectionMenu,label='Connection')
menubarRoot.add_cascade(menu=feedbackMenu, label='Feedback')
menubarRoot.add_cascade(menu=helpMenu, label='Help')

connectionMenu.add_command(label='Connect',command=conWinCall)

feedbackMenu.add_command(label='Report Bug',command=bugRepWinCall)
feedbackMenu.add_command(label='Provide Feedback',command=feedWinCall)

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
content.rowconfigure(1, weight=1)

Body.columnconfigure(0, weight=1)
Body.rowconfigure(0, weight=0)
Body.rowconfigure(1, weight=1)

top_pane.columnconfigure(0, weight=1)
top_pane.columnconfigure(1, weight=1)
top_pane.columnconfigure(2, weight=0)
top_pane.rowconfigure(0, weight=0)
#----------------------------------------------------------------------------------------------------------------------

root.mainloop()
