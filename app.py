'''

GULAG 2.0
GULAG 2.0 is a tkinter based GUI ver. of the original GulagPy with much more
functionality using MySQL.

Authors: Aarav Rajput, Dhruv Arora, Abheek Tripathi

Join The GULAG discord server for programming related doubt solving : https://discord.gg/CE9CafD
Website: https://gulag.heliohost.org

Gulag 2.0 is completely open-source and the code can be used in any way :)

By agreeing to read this code you are sacrificing your soul to satan
because there's no way in hell that you'll be able to read it otherwise

'''
import feedback
import sqlcon
import webbrowser
from tkinter import  *
from tkinter import  ttk
from tkinter import  font
from tkinter import  messagebox
from PIL import ImageTk,Image










#Connection Window
#----------------------------------------------------------------------------------------------------------------------
def conWinCall():

    conCheckStatus = sqlcon.connectSQL('000','000','000')
    optionMenu.entryconfigure('Connect',state='disabled')

    conWin = Toplevel()
    conWin.title('Connection')
    conWin.iconbitmap('gulag.ico')
    conWin.resizable(False,False)

    conFrame=ttk.Frame(conWin,padding="3 3 3 3")
    conFrame.grid(row=0,column=0,padx=5,pady=5)
    
    ttk.Label(conFrame,text='Enter Host\t:').grid(row=0,column=0)
    conHost = ttk.Entry(conFrame)
    conHost.insert(0,'johnny.heliohost.org')
    conHost.grid(row=0,column=1)

    ttk.Label(conFrame,text='Enter Username\t:').grid(row=1,column=0)
    conUsr = ttk.Entry(conFrame)
    conUsr.insert(0,'aarav_')
    conUsr.focus()
    conUsr.grid(row=1,column=1)

    ttk.Label(conFrame,text='Enter Password\t:').grid(row=2,column=0)
    conPswrd = ttk.Entry(conFrame,show="*")
    conPswrd.grid(row=2,column=1)

    def conCheck(*args):
        conCheckStatus = sqlcon.connectSQL(conHost.get(),conUsr.get(),conPswrd.get())
        if conCheckStatus.tf:
            messagebox.showinfo("Connected","Successfully connected to "+conHost.get())
            conWin.destroy()
        else:
            messagebox.showerror("Not Connected","Error: \n"+conCheckStatus.Msg)
            conWin.destroy()

    conPswrd.bind('<Return>',conCheck)


    ttk.Button(conFrame,style='greenButtons.TButton',text="Connect",command=conCheck).grid(row=3,column=1,columnspan=1,pady=10)

    root.wait_window(conWin)
    try:
        if conCheckStatus.tf:
            optionMenu.entryconfigure('Connect',state='disabled',label='Connected to MySQL')
            updateDbBox()
        else:
            optionMenu.entryconfigure('Connect',state='normal')
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
    bugRepWin.geometry('400x330')
    bugRepWin.resizable(False,False)
    bugRepWin.focus()

    bugRepFrame = ttk.Frame(bugRepWin,style='dark.TFrame')
    bugRepFrame.grid(row=0,column=0,stick=(S,W,E,N))

    ttk.Label(bugRepFrame,text='Bug Report',style='mediumDark.TLabel').grid(row=0,column=0,sticky=(W,E))

    BugRepUsrName = ttk.Entry(bugRepFrame)
    BugRepUsrName.insert(0,'Enter your Name')
    BugRepUsrName.grid(row=1,column=0,pady=5,padx=5,sticky=(W,E))

    BugRepUsrMail = ttk.Entry(bugRepFrame)
    BugRepUsrMail.insert(0,'Enter your e-mail')
    BugRepUsrMail.grid(row=2,column=0,pady=5,padx=5,sticky=(W,E))

    BugRepTitle = ttk.Entry(bugRepFrame)
    BugRepTitle.insert(0,'Enter a title (50 characters or less)')
    BugRepTitle.grid(row=3,column=0,pady=5,padx=5,sticky=(W,E))

    bugRepReport = Text(bugRepFrame,wrap='word',width=45,height=9)
    bugRepReport.insert('end','Describe the bug in not more than 250 characters')
    bugRepReport.grid(row=4,column=0,pady=5,padx=5,sticky=(W,E))

    def bugRepSend(*args):
        if ((not '@' in BugRepUsrMail.get()) or (not '.' in BugRepUsrMail.get()) or (' ' in BugRepUsrMail.get()) ):
            messagebox.showerror('Error','Please provide a valid e-mail address so we can contact you')
            BugRepUsrMail.focus()
        elif BugRepUsrName.get() == '' or BugRepUsrName.get() == ' ' or BugRepUsrName.get() == None:
            messagebox.showerror('Error','Please provide a name to that beautiful face :)')
            BugRepUsrName.focus()
        elif bugRepReport.get(1.0,'end') == '' or bugRepReport.get(1.0,'end') == ' ' or bugRepReport.get(1.0,'end') == None:
            messagebox.showerror('Error','Do you even have to really report something ?')
            bugRepReport.focus()
        else:
            try:
                feedback.sendBugReport(BugRepUsrName.get(),BugRepUsrMail.get(),BugRepTitle.get(),bugRepReport.get(1.0,'end'))
                messagebox.showinfo('Success','Thanks for reporting')
                bugRepWin.destroy()
            except:
                messagebox.showinfo('Error','UH OH!! Something went wrong!! Can\'t believe the bug reporting system is bugged xD. Please contact aarav@gulag2.heliohost.org')
                bugRepWin.destroy()

    bugRepBtn = ttk.Button(bugRepFrame,text='SUBMIT',style='greenButtons.TButton',command=bugRepSend)
    bugRepBtn.grid(row=5,column=0,pady=5,padx=5,sticky=(E))

    bugRepWin.rowconfigure(0,weight=1)
    bugRepWin.columnconfigure(0,weight=1)
    
    '''bugRepFrame.rowconfigure(0,weight=0)
                bugRepWin.columnconfigure(0,weight=100)
                bugRepFrame.rowconfigure(1,weight=0)'''

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
    feedWin.geometry('410x300')
    feedWin.resizable(False,False)

    feedbackFrame = ttk.Frame(feedWin,style='dark.TFrame')
    feedbackFrame.grid(row=0,column=0,sticky=(S,W,E,N))

    ttk.Label(feedbackFrame,text='FEEDBACK',style='mediumDark.TLabel').grid(row=0,column=0,sticky=(W,E))

    ttk.Label(feedbackFrame,text='Enter your name :',style='smolDark.TLabel').grid(row=1,column=0,sticky=(W,E),padx=5)
    feedbackUsrName = ttk.Entry(feedbackFrame)
    feedbackUsrName.grid(row=1,column=1,sticky=(W,E),padx=5,pady=5)
    feedbackUsrName.focus()

    ttk.Label(feedbackFrame,text='Please use the slider to show\nhow much you enjoyed our app',style='smolDark.TLabel').grid(row=2,column=0,padx=5,sticky=W)
    feedbackRating = Scale(feedbackFrame, length=200, from_=1, to=5,orient=HORIZONTAL)
    feedbackRating.grid(row=2,column=1,sticky=(E),padx=5,pady=1)

    ttk.Label(feedbackFrame,text='Please describe your experience or give suggestions:',style='smolDark.TLabel').grid(row=3,column=0,sticky=(W),columnspan=2,padx=5)
    feedbackNote = Text(feedbackFrame,wrap='word',width=45,height=7)
    feedbackNote.grid(row=4,column=0,columnspan=2,sticky=(W,E),padx=5)

    def feedbackSend(*args):
        try:
            feedback.sendFeedback(feedbackUsrName.get(),feedbackRating.get(),feedbackNote.get(1.0,'end'))
            messagebox.showinfo('Success','Successfully sent feedback')
            feedWin.destroy()
        except:
            messagebox.showerror('error','Uh!OH! Something went wrong! Please report this bug')
            feedWin.destroy()

    feedbackSubmit = ttk.Button(feedbackFrame,text='SUBMIT',style='greenButtons.TButton',command=feedbackSend)
    feedbackSubmit.grid(row=5,column=1,sticky=E,padx=5,pady=5)

    feedWin.rowconfigure(0,weight=1)
    feedWin.columnconfigure(0,weight=1)

    root.wait_window(feedWin)
    try:
        feedbackMenu.entryconfigure('Provide Feedback',state='normal')
    except:
        return
#----------------------------------------------------------------------------------------------------------------------










#Documentation
#----------------------------------------------------------------------------------------------------------------------
def docsWin():
    webbrowser.open_new_tab('https://www.xenonyx.heliohost.org')
#----------------------------------------------------------------------------------------------------------------------











#Database Creation
#----------------------------------------------------------------------------------------------------------------------
def dbCrWinCall():

    if not sqlcon.testFunc():
        messagebox.showerror('ERROR','You\'re not connected to a server')
        return

    dbCrWin = Toplevel()
    dbCrWin.title('Create Database')
    dbCrWin.iconbitmap('gulag.ico')
    dbCrWin.focus()

    ttk.Label(dbCrWin,text='Enter Database Name\t:').grid(row=0,column=0,pady=2,padx=2)
    dbName = ttk.Entry(dbCrWin)
    dbName.focus()
    dbName.grid(row=0,column=1,padx=2,pady=2)

    def crDBquery(*args):
        try:
            x = sqlcon.crDB(dbName.get())
            if x.tf:
                messagebox.showinfo('Success',x.Msg)
                updateDbBox()
            else:
                messagebox.showerror('Error',x.Msg)
            dbCrWin.destroy()
        except:
            messagebox.showerror('Error','OOPS! Something went wrong\nMake sure you\'re connected to a server\n\nCheck the connection menu')
            dbCrWin.destroy()

    dbName.bind('<Return>',crDBquery)
    ttk.Button(dbCrWin,style='greenButtons.TButton',text='CREATE',command=crDBquery).grid(row=1,column=1,padx=2,pady=2)
#----------------------------------------------------------------------------------------------------------------------










#Table Creation
#----------------------------------------------------------------------------------------------------------------------        
def createTableFunc(*args):

    if not sqlcon.testFunc():
        messagebox.showerror('ERROR','You\'re not connected to a server')
        return

    global colDict
    colDict={}

    messagebox.showinfo('WARNING','This module is currently incapable of detecting and fixing user errors so kindly use it with caution')
    
    #crtbbtn['state']='disabled'
    
    crTWin = Toplevel()
    crTWin.title('Table Creation Wizard')
    crTWin.iconbitmap('gulag.ico')
    crTWin.geometry('600x600')
    
    root.withdraw()

    crTFrame= ttk.Frame(crTWin,style='dark.TFrame')
    crTFrame.grid(row=0,column=0,sticky=(N,S,W,E))

    ttk.Label(crTFrame,text='Enter Table Name',style='mediumDark.TLabel').grid(row=0,column=0)
    
    tab_name_var = StringVar()
    tabName = ttk.Entry(crTFrame,textvariable=tab_name_var)
    tabName.grid(row=0,column=1)
    tabName.focus()

    colFrame = ttk.Frame(crTFrame,style='light.TFrame',padding='10 10 10 10')
    colFrame.grid(row=1,column=0,columnspan=2,sticky=(S,W,E,N))

    colTree = ttk.Treeview(colFrame,selectmode='browse',columns=('Type','NULL','Default'))
    colTree.heading('#0',text='Column Name')
    colTree.heading('Type',text='Type')
    colTree.heading('NULL',text='NULL')
    colTree.heading('Default',text='Default Value')

    colTree.column('#0',width=60)
    colTree.column('Type',width=100)
    colTree.column('NULL',width=15)
    colTree.column('Default',width=60)

    colTree.grid(row=0,column=0,sticky=(N,S,W,E))

    colTreeScroll = ttk.Scrollbar(crTFrame,orient=VERTICAL,command=colTree.yview)
    colTreeScroll.grid(row=1,column=2,sticky=(N,S))
    colTree['yscrollcommand']=colTreeScroll.set

    colTreeHScroll = ttk.Scrollbar(crTFrame,orient=HORIZONTAL,command=colTree.xview)
    colTreeHScroll.grid(row=2,column=0,columnspan=2,sticky=(E,W))
    colTree['xscrollcommand']=colTreeHScroll.set

    colConsole = ttk.Frame(crTFrame,style='dark.TFrame')
    colConsole.grid(row=4,column=0,padx = 10 , pady = 5,columnspan=3)

    def addColWinCall():
        messagebox.showinfo('WARNING','This module is currently incapable of detecting and fixing user errors so kindly use it with caution')
        crTWin.withdraw()
        addColWin = Toplevel()
        addColWin.title('Add Column')
        addColWin.iconbitmap('gulag.ico')

        addColFrame = ttk.Frame(addColWin,style='light.TFrame',padding='3 3 3 3')
        addColFrame.grid(row=0,column=0)

        ttk.Label(addColFrame,text='Column Name\t:\t',style='smolLight.TLabel').grid(row=0,column=0,sticky=(W,E,N,S))
        ttk.Label(addColFrame,text='Column Type\t:\t',style='smolLight.TLabel').grid(row=1,column=0,sticky=(W,E,N,S))
        ttk.Label(addColFrame,text='NULL       \t:\t',style='smolLight.TLabel').grid(row=4,column=0,sticky=(W,E,N,S))
        ttk.Label(addColFrame,text='Default    \t:\t',style='smolLight.TLabel').grid(row=5,column=0,sticky=(W,E,N,S))

        global col_name_var
        col_name_var = StringVar()

        colName = ttk.Entry(addColFrame,textvariable=col_name_var)
        colName.grid(row=0,column=1,sticky=(W,E,N,S),pady=5)
        colName.focus()

        global col_type_var
        col_type_var = StringVar()

        def selectType(*args):
            if col_type_var.get() == 'Decimal':
                colSizeWin = Toplevel()
                colSizeWin.title('Column Config')
                colSizeWin.iconbitmap('gulag.ico')
                addColWin.withdraw()

                colSizeFrame = ttk.Frame(colSizeWin,style='light.TFrame')
                colSizeFrame.grid(row=0,column=0)

                global col_dec_tot
                col_dec_tot = StringVar()

                ttk.Label(colSizeFrame,text='Total decimal digits\t:\t',style='smolLight.TLabel').grid(row=0,column=0)
                x = ttk.Entry(colSizeFrame,textvariable=col_dec_tot)
                x.grid(row=0,column=1)
                x.focus()

                global col_dec_aft
                col_dec_aft = StringVar()

                ttk.Label(colSizeFrame,text='Decimal Position\t:\t',style='smolLight.TLabel').grid(row=1,column=0)
                ttk.Entry(colSizeFrame,textvariable=col_dec_aft).grid(row=1,column=1)

                ttk.Button(colSizeFrame,text='OK',command=colSizeWin.destroy).grid(row=2,column=1,pady=5)

                addColWin.wait_window(colSizeWin)
                try:
                    addColWin.deiconify()
                except:
                    return

            elif col_type_var.get() == 'Varchar' or col_type_var.get()=='Char' or col_type_var.get() == 'Integer':
                colSizeWin = Toplevel()
                colSizeWin.title('Column Config')
                colSizeWin.iconbitmap('gulag.ico')
                addColWin.withdraw()

                colSizeFrame = ttk.Frame(colSizeWin,style='light.TFrame')
                colSizeFrame.grid(row=0,column=0)

                global col_size
                col_size = StringVar()

                ttk.Label(colSizeFrame,text='Size\t:\t',style='smolLight.TLabel').grid(row=0,column=0)
                x = ttk.Entry(colSizeFrame,textvariable=col_size)
                x.grid(row=0,column=1)
                x.focus()

                ttk.Button(colSizeFrame,text='OK',command=colSizeWin.destroy).grid(row=2,column=1,pady=5)

                addColWin.wait_window(colSizeWin)
                try:
                    addColWin.deiconify()
                except:
                    return
 
        col_type = ttk.Combobox(addColFrame,textvariable=col_type_var,state='readonly')
        col_type.grid(row=1,column=1,sticky=(S,W,E,N),pady=5)
        col_type['values']=('Integer','Decimal','Char','Varchar','Date','Time','Boolean','Date')
        col_type.bind('<<ComboboxSelected>>',selectType)

        global col_null_var
        col_null_var = StringVar()

        col_null = ttk.Combobox(addColFrame,textvariable=col_null_var,state='readonly')
        col_null.grid(row=4,column=1,sticky=(E,W,N,S),pady=5)
        col_null['values']=('','NOT NULL')

        global col_default_var
        col_default_var = StringVar()

        ttk.Entry(addColFrame,textvariable=col_default_var).grid(row=5,column=1,sticky=(S,W,E,N),pady=5)





        def addColCom():
            if col_name_var.get() == '' or col_type_var.get() == '':
                messagebox.showerror('ERROR','Column name and type can not be empty !!')
                colName.focus()
                return
            if col_type_var.get() == 'Decimal':
                colTree.insert('','end',text=col_name_var.get(),values=(col_type_var.get()+'('+col_dec_tot.get()+','+col_dec_aft.get()+')',col_null_var.get(),col_default_var.get()))
                addColWin.destroy()
            elif col_type_var.get() == 'Char' or col_type_var.get() == 'Varchar' or col_type_var.get() == 'Integer':
                colTree.insert('','end',text=col_name_var.get(),values=(col_type_var.get()+'('+col_size.get()+')',col_null_var.get(),col_default_var.get()))
                addColWin.destroy()
            else:
                colTree.insert('','end',text=col_name_var.get(),values=(col_type_var.get(),col_null_var.get(),col_default_var.get()))
                addColWin.destroy()
            colDict[colTree.item(colTree.get_children()[-1])['text']] = colTree.item(colTree.get_children()[-1])['values']





        addcolbtn = ttk.Button(addColFrame,text='ADD',style='greenButtons.TButton',command=addColCom)
        addcolbtn.grid(row=7,column=1)

        addColFrame.columnconfigure(0,weight=1)

        crTWin.wait_window(addColWin)
        try:
            crTWin.deiconify()
        except:
            return

    def finaliseColCall(*args):
        createTableButton['state']='disabled'
        global prim_var
        prim_var = StringVar()

        keyDefWin = Toplevel()
        keyDefWin.title('Define primary key')
        keyDefWin.iconbitmap('gulag.ico')

        colsList = list(colDict.keys())

        keyFrame = ttk.Frame(keyDefWin,style='dark.TFrame',padding='5 5 5 5')
        keyFrame.grid(row=0,column=0,sticky=(N,S,W,E))

        ttk.Label(keyFrame,text='Primary Key',style='smolLight.TLabel').grid(row=0,column=0)
        prim = ttk.Combobox(keyFrame,textvariable=prim_var,values=colsList,state='readonly')
        prim.grid(row=0,column=1,sticky=(S,W,E,N),pady=10)
        prim.focus()

        def checkPrimNull(*args):
            if prim_var.get() == '' or prim_var.get() == None or prim_var.get() == ' ':
                messagebox.showerror('Error','Primary Key can\'t be null')
            else:
                keyDefWin.destroy()

        ttk.Button(keyFrame,text='OK',command=checkPrimNull).grid(row=1,column=1)

        crTWin.wait_window(keyDefWin)
        try:
            createTableButton['state']='disabled'
        except:
            return
    
    addCol = ttk.Button(colConsole,text='Add Column',style='greenButtons.TButton',command=addColWinCall)
    addCol.grid(row=0,column=0,padx=5)

    def delColCall(*args):
        try:
            colDict.pop(colTree.item(colTree.selection()[0])['text'])
            colTree.delete(colTree.selection()[0])
        except:
            messagebox.showerror('Error','Did you select a column to delete ??')

    delCol = ttk.Button(colConsole,text='Delete Column',style='redButtons.TButton',command=delColCall)
    delCol.grid(row=0,column=1,padx=5)

    def createTableCheck(*args):
        try:
            if tabName.get() == '' or tabName.get() == ' ':
                messagebox.showerror("ERROR",'Table Name can\'t be empty')
                return

            finaliseColCall()
            col_command = ''
                
            for i in colDict.keys():
                v = colDict[i]
                col_command += i+' '
                for j in v:
                    if not j == '' or j == ' ':
                        col_command += j+' '
                col_command += ','
                
            col_command = col_command
            col_comm = 'CREATE TABLE '+tabName.get()+'('+col_command+'PRIMARY KEY ('+prim_var.get()+'))'
            try:
                x = sqlcon.givcommand(col_comm)
                if x.tf:
                    messagebox.showinfo('Success','Table created successfully')
                    crTWin.destroy()
                    updateTbBox()
                else:
                    messagebox.showerror('ERROR','Command: '+col_comm+'\n\n\n'+x.Msg)
                    createTableButton['state']='normal'
            except:
                messagebox.showerror("ERROR",'Error in creating table')
                createTableButton['state']='normal'
        except:
            messagebox.showerror("ERROR","Something went wrong! Please report this bug")
            crTWin.destroy()

    createTableButton = ttk.Button(crTFrame,text='Create Table',style='greenButtons.TButton',command=createTableCheck)
    createTableButton.grid(row=5,column=1)

    crTWin.columnconfigure(0,weight=1)
    crTWin.rowconfigure(0,weight=1)

    crTFrame.columnconfigure(0,weight=1)
    crTFrame.columnconfigure(1,weight=1)
    crTFrame.rowconfigure(1,weight=1)

    colFrame.columnconfigure(0,weight=1)
    colFrame.rowconfigure(0,weight=1)

    root.wait_window(crTWin)
    try:
        #crtbbtn['state']='normal'
        root.deiconify()
    except:
        return
#----------------------------------------------------------------------------------------------------------------------










#Developer Window
#----------------------------------------------------------------------------------------------------------------------
def devWinCall():
    optionMenu.entryconfigure('Developer Console',state='disabled')
    devWin = Toplevel()
    devWin.title("DEVELOPER CONSOLE")
    devWin.iconbitmap('gulag.ico')
    devWin.geometry('600x300')

    devFrame= ttk.Frame(devWin,style='dark.TFrame')
    devFrame.grid(row=0,column=0,sticky=(N,S,W,E))

    ttk.Label(devFrame,text='Input Command\t:\t',style='smolDark.TLabel').grid(row=0,column=0,padx=5,pady=5)
    console = ttk.Entry(devFrame)
    console.grid(row=0,column=1)
    console.focus()

    def pushCom(*args):
        try:
            x = sqlcon.givcommand(console.get())
            console.delete(0,'end')
            if x.tf:
                outputFrame.insert('end',x.Msg)
            else:
                outputFrame.insert('end',x.Msg)
                outputFrame.itemconfigure('end',background='#e06f60')
        except:
            messagebox.showerror('Error',"OOPS!! Something went wrong\nMake sure you're connected to a MySQL server")
            console.focus()
    console.bind('<Return>',pushCom)

    outputFrame = Listbox(devWin,background='#a9aaab')
    outputFrame.grid(row=1,column=0,sticky=(N,S,W,E))
    outputVScroll = Scrollbar(devWin,orient=VERTICAL,command=outputFrame.yview)
    outputVScroll.grid(row=1,column=1,sticky=(N,S))
    outputFrame['yscrollcommand']=outputVScroll.set
    outputHScroll = Scrollbar(devWin,orient=HORIZONTAL,command=outputFrame.xview)
    outputHScroll.grid(row=2,column=0,sticky=(E,W))
    outputFrame['xscrollcommand']=outputHScroll.set

    devWin.columnconfigure(0,weight=1)
    devWin.rowconfigure(0,weight=0)
    devWin.rowconfigure(1,weight=1)

    root.wait_window(devWin)
    try:
        optionMenu.entryconfigure('Developer Console',state='normal')
    except:
        return

#----------------------------------------------------------------------------------------------------------------------










#Add Record
#----------------------------------------------------------------------------------------------------------------------
def addRecordCall(*args):
    try:
        addRecWin = Toplevel()
        addRecWin.title('Add Record')
        #addRecBtn['state'] = 'disabled'
        addRecWin.iconbitmap('gulag.ico')

        root.withdraw()

        addRecFrame = ttk.Frame(addRecWin,style='dark.TFrame')
        addRecFrame.grid(row=0,column=0,sticky=(N,S,W,E))

        x = sqlcon.returnAllColList(tb_var.get())
        recEntries = []
        c=0
        for i in x:
            ttk.Label(addRecFrame,text=str(i),style='smolDark.TLabel').grid(row=c,column=0,sticky=(W,E))
            e = ttk.Entry(addRecFrame)
            e.grid(row=c,column=1,padx=10,pady=10,sticky=(E,W))
            e.focus()
            recEntries.append(e)
            c+=1

        def sendAddComm(*args):

            def checkColumnType():
                try:
                    x = sqlcon.returnColType(tb_var.get())
                    if x.tf:
                        global columnType
                        columnType = x.Msg
                    else:
                        messagebox.showerror('ERROR',x.Msg)
                except:
                    messagebox.showerror('ERROR','OOPS!! Something went wrong!\nPlease Report this bug')

            def checkNull():
                try:
                    x = sqlcon.returnNotNull(tb_var.get())
                    if x.tf:
                        global notnull
                        notnull = x.Msg
                    else:
                        messagebox.showerror('ERROR',x.Msg)
                except:
                    messagebox.showerror('ERROR','OOPS!! SOmething went wrong\nPlease report this bug')

            checkColumnType()
            checkNull()
            values = ''
            for i in range(len(recEntries)):
                e = recEntries[i]
                t = columnType[i]
                if i in notnull and e.get()=='':
                    messagebox.showerror('ERROR','Column no. '+str(i)+' can not be null')
                    e.focus()
                    return
                else:
                    if t[:7]==b'varchar' or t[:4]==b'char' or t[:7]=='varchar' or t[:4]=='char' or t[:4] == 'text':
                        if not e.get()=='':
                            values += '\''+str(e.get())+'\''+','
                        else:
                            values += 'NULL,'
                    elif t==b'date' or t=='date':
                        if not e.get()=='':
                            values+='\''+str(e.get())+'\''+','
                        else:
                            values+='NULL,'
                    else:
                        if not e.get()=='':
                            values +=str(e.get())+','
                        else:
                            values += 'NULL,'

            x = sqlcon.addRecFunc(tb_var.get(),values[:-1])
            if x.tf:
                messagebox.showinfo('Success',x.Msg)
                addRecWin.destroy()
                actuallyUpdateRecords()
            else:
                messagebox.showerror('Error',x.Msg)
                recEntries[-1].focus()
                return

        ttk.Button(addRecFrame,text='ADD',style='greenButtons.TButton',command = sendAddComm).grid(row=c,column=1,sticky=(E,W))

        addRecWin.columnconfigure(0,weight=1)
        addRecWin.columnconfigure(1,weight=1)
        addRecWin.rowconfigure(0,weight=1)
        addRecWin.rowconfigure(1,weight=1)

        root.wait_window(addRecWin)
        try:
            #addRecBtn['state']='normal'
            root.deiconify()
        except:
            return

    except:
        addRecWin.destroy()
        messagebox.showerror('ERROR','Something went wrong!!\nDid you select a table ?¿')
        #addRecBtn['state']='normal'
        root.deiconify()
#----------------------------------------------------------------------------------------------------------------------










#Delete Record
#----------------------------------------------------------------------------------------------------------------------
def delRecordCall(*args):
    c = messagebox.askyesno('Delete Record','Are you sure you want to delete the record?')
    if c:
        try:
            x = sqlcon.returnPrimaryKey(tb_var.get())
            if x.tf:
                primValue = recTree.item(recTree.selection()[0])['values'][x.Msg[0]]
                primName = x.Msg[1]

                try:
                    y = sqlcon.deleteRecord(tb_var.get(),primName,primValue)
                    if y.tf:
                        messagebox.showinfo('Success',y.Msg)
                        actuallyUpdateRecords()
                    else:
                        messagebox.showerror('Error',y.Msg)
                except:
                    messagebox.showerror('Error','Couldn\'t delete the record')
            else:
                messagebox.showerror('Error',x.Msg)
        except:
            messagebox.showerror('ERROR','Could not detect primary key!! Aborting')
    else:
        messagebox.showinfo('WARNING','Be Careful of the buttons you touch')
#----------------------------------------------------------------------------------------------------------------------










#Update Record
#----------------------------------------------------------------------------------------------------------------------

def updateRecordCall(*args):
    c = messagebox.askyesno('Delete Record','Are you sure you want to update the record?')
    if c:
        updateRecordWin = Toplevel()
        updateRecordWin.title('UPDATE RECORD')
        updateRecordWin.iconbitmap('gulag.ico')
        updateRecordWin.columnconfigure(0,weight=1)
        updateRecordWin.rowconfigure(0,weight=1)

        root.withdraw()

        updateFrame = ttk.Frame(updateRecordWin,padding='5 5 5 5',style='dark.TFrame')
        updateFrame.grid(row=0,column=0,sticky=(S,W,E,N))


        try:
            columnList = sqlcon.returnAllColList(tb_var.get())
            recEntries = []
            c=0
            for i in columnList:
                ttk.Label(updateFrame,text=str(i),style='smolDark.TLabel').grid(row=c,column=0,sticky=(W,E))
                e = ttk.Entry(updateFrame)
                e.grid(row=c,column=1,padx=10,pady=10,sticky=(E,W))
                e.focus()
                recEntries.append(e)
                c+=1
            try:
                x = sqlcon.returnPrimaryKey(tb_var.get())
                if x.tf:
                    primValue = recTree.item(recTree.selection()[0])['values'][x.Msg[0]]
                    primName = x.Msg[1]
                else:
                    messagebox.showerror('Error',x.Msg)
            except:
                messagebox.showerror('ERROR','Did You select a record')
                updateRecordWin.destroy()
                root.deiconify()
                return


            try:
                c=0
                for entry in recEntries:

                    entry.insert(0,recTree.item(recTree.selection()[0])['values'][c])
                    c+=1
            except:
                messagebox.showerror('ERROR','OOPS!! Something went wrong\nReport this bug immediately')
                updateRecordWin.destroy()
                root.deiconify()
                return

            def sendUpdateComm(clist,primary,valprim,*args):

                def checkColumnType():
                    try:
                        x = sqlcon.returnColType(tb_var.get())
                        if x.tf:
                            global columnType
                            columnType = x.Msg
                        else:
                            messagebox.showerror('ERROR',x.Msg)
                    except:
                        messagebox.showerror('ERROR','OOPS!! Something went wrong!\nPlease Report this bug')
                        return

                def checkNull():
                    try:
                        x = sqlcon.returnNotNull(tb_var.get())
                        if x.tf:
                            global notnull
                            notnull = x.Msg
                        else:
                            messagebox.showerror('ERROR',x.Msg)
                    except:
                        messagebox.showerror('ERROR','OOPS!! SOmething went wrong\nPlease report this bug')
                        return

                checkColumnType()
                checkNull()
                values = []
                for i in range(len(recEntries)):
                    e = recEntries[i]
                    t = columnType[i]
                    if i in notnull and (e.get()=='' or e.get()=='None' or e.get() == 'NULL'):
                        messagebox.showerror('ERROR','Column no. '+str(i)+' can not be null')
                        e.focus()
                        return
                    else:
                        if t[:7]==b'varchar' or t[:4]==b'char' or t[:7]=='varchar' or t[:4]=='char':
                            if not e.get()=='' or e.get()=='None' or e.get()=='NULL':
                                values.append('\''+str(e.get())+'\'')
                            else:
                                values.append('NULL')
                        elif t==b'date' or t=='date':
                            if not e.get()=='' or e.get()=='None' or e.get()=='NULL':
                                values.append('\''+str(e.get())+'\'')
                            else:
                                values.append('NULL')
                        else:
                            if not e.get()=='' or e.get()=='None' or e.get()=='NULL':
                                values.append(str(e.get()))
                            else:
                                values.append(str(e.get()))

                setlist=''
                for i in range(len(values)):
                    setlist += str(clist[i])+' = '+values[i]+', '

                sndCom = sqlcon.upRecFunc(str(tb_var.get()),str(setlist),str(primary),str(valprim))
                
                if sndCom.tf:
                    messagebox.showinfo('Success',sndCom.Msg)
                    updateRecordWin.destroy()
                    root.deiconify()
                    actuallyUpdateRecords()
                else:
                    messagebox.showerror('Error',sndCom.Msg)
                    updateRecordWin.destroy()
                    root.deiconify()

            ttk.Button(updateFrame,text='UPDATE',style='greenButtons.TButton',command=lambda: sendUpdateComm(clist=columnList,primary=primName,valprim=primValue)).grid(row=c,column=1,padx=10,pady=10)

        except:
            messagebox.showerror('ERROR','OOPS!! Something went wrong\nDid you select a table ?\nReport this bug if yes')
            updateRecordWin.destroy()
            root.deiconify()

        try:
            root.wait_window(updateRecordWin)
            root.deiconify()
        except:
            return
    else:
        messagebox.showinfo('WARNING','Be Careful of the buttons you touch')
#----------------------------------------------------------------------------------------------------------------------










#Functions
#----------------------------------------------------------------------------------------------------------------------
def selectDB(*args):
    try:
        x=sqlcon.use(db_listbox.get(db_listbox.curselection()))
        messagebox.showinfo("Database Select",x)
        updateTbBox()
    except:
        messagebox.showerror("Error","Database not selected\nMake sure you're connected\n\nGo to the connection menu")

def updateDbBox():
    clearDB()
    dbListVar = sqlcon.returnDbList()
    for i in dbListVar:
        db_listbox.insert('end',i)
    updateTbBox()

def clearDB(*args):
    dbListVar = db_listbox.get(0,END)
    for i in dbListVar:
        db_listbox.delete(db_listbox.get(0,END).index(i))

def dbDropFunc(*args):
    confirm = messagebox.askyesno('DROP Database ?¿','Are you sure you would like to drop the database ???')
    if confirm==True:
        try:
            x = sqlcon.dropDB(db_listbox.get(db_listbox.curselection()))
            if x.tf:
                messagebox.showinfo('Success',x.Msg)
                updateDbBox()
            else:
                messagebox.showerror('Error',x.Msg)
        except:
            messagebox.showerror('Error','OOPS! Something went wrong\nDid you select a database ?¿')
    else:
        messagebox.showinfo('?¿?¿','Be careful of the buttons you touch...')

def tbDelFunc(*args):
    confirm = messagebox.askyesno('Delete table ?¿','Are you sure you would like to delete the table ???')
    if confirm==True:
        try:
            x = sqlcon.deltab(tb_var.get())
            if x.tf:
                messagebox.showinfo('Success',x.Msg)
                updateTbBox()
            else:
                messagebox.showerror('Error',x.Msg)
        except:
            messagebox.showerror('Error','OOPS! Something went wrong\nDid you select a table ?¿')
    else:
        messagebox.showinfo('?¿?¿','Be careful of the buttons you touch...')

def tbTruncFunc(*args):
    confirm = messagebox.askyesno('Truncate table ?¿','Are you sure you would like to truncate the table ???')
    if confirm==True:
        try:
            x = sqlcon.trun(tb_var.get())
            if x.tf:
                messagebox.showinfo('Success',x.Msg)
                actuallyUpdateRecords()
            else:
                messagebox.showerror('Error',x.Msg)
        except:
            messagebox.showerror('Error','OOPS! Something went wrong\nDid you select a table ?¿')
    else:
        messagebox.showinfo('?¿?¿','Be careful of the buttons you touch...')

def clearTB(*args):
    tbListVar = tb_listbox.get(0,END)
    for i in tbListVar:
        tb_listbox.delete(tb_listbox.get(0,END).index(i))
        
def updateTbBox(*args):
    clearTB()
    tbListVar = sqlcon.returnTbList()
    for i in tbListVar:
        tb_listbox.insert('end',i)

def clearRecs(*args):
    try:
        recTree.delete(*recTree.get_children())
    except:
        messagebox.showerror("ERROR",'Can\'t clear')

def updateRecordTree(*args):
    try:
        queryColS.set('')
        queryVar.set('')
        x = sqlcon.returnAllColList(tb_var.get())
        recTree['columns']=tuple(x)
        queryCol['values']=tuple(x)
        queryCol.current(0)
        counter=0
        widlist = sqlcon.returnMaxLengthCol(tb_var.get())
        if widlist.tf:
            for i in x:
                recTree.heading(str(i),text=str(i),anchor='sw')
                recTree.column(str(i),width=((list(widlist.Msg)[counter])*5)+30)
                counter+=1
        else:
            messagebox.showerror('Error','OOPS! Something went wrong\nPlease report this bug immediately')

    except:
        messagebox.showerror("Error","Something Went Wrong \nPlease Report the bug")

def actuallyUpdateRecords(*args):
    clearRecs()
    updateRecordTree()
    x = sqlcon.showall(tb_var.get())
    for i in x:
        recTree.insert('','end',values=tuple(i))


'''def updateTableDesc():
    try:
        x=sqlcon.returnTableDefinition(tb_var.get())
    except:
        messagebox.showerror('ERROR','Something went wrong \nPlease report this bug')
'''

def selectTable(*args):
    try:
        global tb_var
        tb_var = StringVar()
        tb_var.set(tb_listbox.get(tb_listbox.curselection()))
        actuallyUpdateRecords()
#        updateTableDesc()
    except:
        messagebox.showerror('Error','Something went wrong \nPlease report this bug')

def queryCall(*args):
    try:
        x = sqlcon.query(tb_var.get(),queryColS.get(),queryVar.get())
        if x.tf:
            clearRecs()
            #updateRecordTree()
            for msgval in x.Msg:
                recTree.insert('','end',values=msgval)
        else:
            messagebox.showerror('ERROR',x.Msg)
    except:
        messagebox.showerror('ERROR','Something went wrong \nPlease report this bug')

def commit(*args):
    y = messagebox.askyesno('COMMIT','Are you sure you would like to commit the changes ??')
    if y:
        try:
            x=sqlcon.commitall()
            if x:
                messagebox.showinfo('Success','Successfully committed changes')
            else:
                messagebox.showerror('Error','Could not commit')
        except:
            messagebox.showerror('ERROR','OOPS!! Something went wrong\nPlease report this bug')
    else:
        messagebox.showinfo('WARNING','Be Careful of the buttons you touch')

def dbrootreq(*args):
    helpMenu.entryconfigure('Request database root',state='disabled')

    requestWindow = Toplevel()
    requestWindow.title('DB Root Request')
    requestWindow.iconbitmap('gulag.ico')
    requestWindow.geometry('400x330')
    requestWindow.resizable(False,False)
    requestWindow.focus()

    requestFrame = ttk.Frame(requestWindow,style='light.TFrame')
    requestFrame.grid(row=0,column=0,sticky=(S,W,E,N))

    requestName = ttk.Entry(requestFrame)
    requestName.insert(0,'Enter your name')
    requestName.grid(row=0,column=0,sticky=(W),padx=5,pady=5)

    requestEmail = ttk.Entry(requestFrame)
    requestEmail.insert(0,'Enter your email')
    requestEmail.grid(row=1,column=0,sticky=(W),padx=5,pady=5)

    requestReason = Text(requestFrame,wrap='word',width=45,height=7)
    requestReason.insert(1.0,'Give us a valid reason why we should give you access to the server root account (under 250 characters)')
    requestReason.grid(row=2,column=0,sticky=(W,E),padx=5)

    def submitRequest(*args):
        try:
            feedback.sendRootRequest(requestName.get(),requestEmail.get(),requestReason.get(1.0,'end'))
            messagebox.showinfo('Success','Successfully sent request. An admin will contact you shortly')
            requestWindow.destroy()
        except:
            messagebox.showerror('Error','Something went wrong \nPlease report this bug')
            requestWindow.destroy()

    requestSubmit = ttk.Button(requestFrame,text='SUBMIT',style='greenButtons.TButton',command=submitRequest)
    requestSubmit.grid(row=3,column=0,sticky=E,padx=5)

    requestWindow.rowconfigure(0,weight=1)
    requestWindow.columnconfigure(0,weight=1)

    root.wait_window(requestWindow)
    try:
        helpMenu.entryconfigure('Request database root',state='normal')
    except:
        return


#----------------------------------------------------------------------------------------------------------------------









#Root Window
#----------------------------------------------------------------------------------------------------------------------
root = Tk()
root.iconbitmap('gulag.ico')
root.title('GULAG 2.0 (Open Beta)')
root.geometry('800x600')
root.minsize(width=800,height=600)
#----------------------------------------------------------------------------------------------------------------------









#Styles Handling
#----------------------------------------------------------------------------------------------------------------------
styleHandle = ttk.Style()
styleHandle.configure('greenButtons.TButton',background='green',foreground='green')
styleHandle.configure('redButtons.TButton',background='red',foreground='red')
styleHandle.configure('blueButtons.TButton',background='blue',foreground='blue')

bigFont = font.Font(family='Bahnschrift SemiBold Condensed',size=40,weight='bold')
mediumFont = font.Font(family='Helvetica',size=20,weight='bold')
smolFont = font.Font(family='Helvetica',size=10)

styleHandle.configure('bigDark.TLabel',background='#4a4d4f',foreground='#a9aaab',font=bigFont)
styleHandle.configure('bigLight.TLabel',background='#a9aaab',foreground='#4a4d4f',font=bigFont)

styleHandle.configure('mediumDark.TLabel',background='#4a4d4f',foreground='#a9aaab',font=mediumFont)
styleHandle.configure('mediumLight.TLabel',background='#a9aaab',foreground='#4a4d4f',font=mediumFont)

styleHandle.configure('smolDark.TLabel',background='#4a4d4f',foreground='#a9aaab',font=smolFont)
styleHandle.configure('smolLight.TLabel',background='#a9aaab',foreground='#4a4d4f',font=smolFont)

styleHandle.configure('dark.TLabel',background='#4a4d4f',foreground='#a9aaab')
styleHandle.configure('light.TLabel',background='#a9aaab',foreground='#4a4d4f')

styleHandle.configure('dark.TFrame',background='#4a4d4f',foreground='#a9aaab')
styleHandle.configure('light.TFrame',background='#a9aaab',foreground='#4a4d4f')

#styleHandle.configure('Horizontal.dark.TScale',background='#4a4d4f',lightcolor='#a9aaab')

#----------------------------------------------------------------------------------------------------------------------








#TORMENT OF MY BRAIN [DO NOT TRY TO MAKE A SENSE OUT OF IT // IT DOESN'T]
#----------------------------------------------------------------------------------------------------------------------
content = ttk.Frame(root,style='dark.TFrame')
content.grid(sticky=(N,E,W,S))

Header = ttk.Frame(content,padding=(5,5,5,5),style='dark.TFrame')
Header.grid(row=0,column=0,sticky=(N,E,W,S),padx=5,pady=0)

logo = ImageTk.PhotoImage(Image.open('Gulag.png'))
ttk.Label(Header,image=logo,style='dark.TLabel').grid(row=0,column=0,sticky=W)
ttk.Label(Header,text="GULAG 2.0",style='bigDark.TLabel').grid(row=0,column=1,sticky=E)

Body = ttk.Frame(content,width=590,height=350,style='light.TFrame')
Body.grid(row=1,column=0,padx=10,pady=5,sticky=(N,E,W,S))










top_pane = ttk.Frame(Body)
top_pane.grid(row=0,column=0,columnspan=2,sticky=(N,E,W,S))




db_frame = ttk.Labelframe(top_pane, text='Databases',padding='3 3 3 3')
db_frame.grid(row=0,column=0,sticky=(S,W,E,N),padx=5)

db_listbox = Listbox(db_frame,height=5)
db_listbox.grid(row=0,column=0,sticky=(S,W,E,N))
dbScroller = ttk.Scrollbar(db_frame,orient=VERTICAL,command=db_listbox.yview)
dbScroller.grid(row=0,column=1,sticky=(N,S,E,W))
db_listbox['yscrollcommand']=dbScroller.set
db_listbox.bind('<Double-1>', selectDB)
db_listbox.bind('<Return>', selectDB)

db_console = ttk.Frame(db_frame)
db_console.grid(row=1,column=0,sticky=(N,E,W,S))

crdbbtn = ttk.Button(db_console,text='CREATE',style='greenButtons.TButton', command=dbCrWinCall)
crdbbtn.grid(row=0,column=0,padx=2,pady=2)
drdbbtn = ttk.Button(db_console,text='DROP',style='redButtons.TButton', command=dbDropFunc)
drdbbtn.grid(row=0,column=1,padx=2,pady=2)




tb_frame = ttk.Labelframe(top_pane, text='Tables',padding='3 3 3 3')
tb_frame.grid(row=0,column=1,sticky=(S,W,E,N),padx=5)

tb_listbox = Listbox(tb_frame,height=5)
tb_listbox.grid(row=0,column=0,sticky=(N,E,W,S))
tbScroller = ttk.Scrollbar(tb_frame,orient=VERTICAL,command=tb_listbox.yview)
tbScroller.grid(row=0,column=1,sticky=(N,S,W,E))
tb_listbox['yscrollcommand']=tbScroller.set
tb_listbox.bind('<Double-1>', selectTable)
tb_listbox.bind('<Return>', selectTable)

tb_console = ttk.Frame(tb_frame)
tb_console.grid(row=1,column=0,sticky=(N,E,W,S))

crtbbtn = ttk.Button(tb_console,text='CREATE',style='greenButtons.TButton',command=createTableFunc)
crtbbtn.grid(row=0,column=0,padx=2,pady=2)
deltbbtn = ttk.Button(tb_console,text='DELETE',style='redButtons.TButton',command=tbDelFunc)
deltbbtn.grid(row=0,column=1,padx=2,pady=2)
truntbbtn = ttk.Button(tb_console,text='TRUNCATE',style='blueButtons.TButton',command=tbTruncFunc)
truntbbtn.grid(row=0,column=2,padx=2,pady=2)










mainApp = ttk.Notebook(Body)
mainApp.grid(row=1,column=0,sticky=(N,E,W,S))






records_tab = ttk.Frame(mainApp)
mainApp.add(records_tab,text='Records')

recQuery = ttk.Frame(records_tab,style='light.TFrame',padding='3 3 3 3')
recQuery.grid(row=0,column=0,columnspan=3,sticky=(S,W,E,N))

global queryColS
queryColS = StringVar()
ttk.Label(recQuery,text='Search By:  ',style='smolLight.TLabel').grid(row=0,column=0,sticky=(S,W,E,N))
queryCol = ttk.Combobox(recQuery,textvariable=queryColS,state='readonly')
queryCol.grid(row=0,column=1,sticky=(W,E))

global queryVar
queryVar=StringVar()
ttk.Label(recQuery,text='Search: ',style='smolLight.TLabel').grid(row=0,column=0,sticky=(S,W,E,N))
ttk.Entry(recQuery,textvariable=queryVar).grid(row=0,column=3,sticky=(W,E),padx=10)

qicon = ImageTk.PhotoImage(Image.open('search.png'))
ttk.Button(recQuery,image=qicon,style='greenButtons.TButton',command=queryCall).grid(row=0,column=4,sticky=W)






recFrame = ttk.Frame(records_tab,style='light.TFrame',padding='3 3 3 3')
recFrame.grid(row=1,column=0,sticky=(N,S,W,E))

recTree = ttk.Treeview(recFrame,selectmode='browse',show='headings')
recTree.column('#0',width=0)
recTree.grid(row=0,column=0,sticky=(N,S,W,E))

treeScroll = ttk.Scrollbar(recFrame,orient=VERTICAL,command=recTree.yview)
treeScroll.grid(row=0,column=1,sticky=(N,S))
recTree['yscrollcommand']=treeScroll.set

treeHScroll = ttk.Scrollbar(recFrame,orient=HORIZONTAL,command=recTree.xview)
treeHScroll.grid(row=1,column=0,sticky=(E,W))
recTree['xscrollcommand']=treeHScroll.set





recConsole = ttk.Frame(records_tab,style='dark.TFrame')
recConsole.grid(row=1,column=1,sticky=(N,S,W,E))

addRecBtn = ttk.Button(recConsole,text='ADD RECORD',style='greenButtons.TButton',command=addRecordCall)
addRecBtn.grid(row=0,column=0,pady=10,padx=10,sticky=(N,S,W,E))

delRecBtn = ttk.Button(recConsole,text='DELETE RECORD',style='redButtons.TButton',command=delRecordCall)
delRecBtn.grid(row=1,column=0,pady=10,padx=10,sticky=(N,S,W,E))

upRecBtn = ttk.Button(recConsole,text='UPDATE RECORD',style='blueButtons.TButton',command=updateRecordCall)
upRecBtn.grid(row=2,column=0,pady=10,padx=10,sticky=(N,S,W,E))

commitBtn = ttk.Button(recConsole,text='COMMIT',style='greenButtons.TButton',command=commit)
commitBtn.grid(row=3,column=0,padx=10,pady=10,sticky=(N,S,W,E))






'''tbEditFrame = ttk.Frame(mainApp)
mainApp.add(tbEditFrame,text='Edit Table')

tableDesc = ttk.Frame(tbEditFrame,style='dark.TFrame',padding='3 3 3 3')
tableDesc.grid(row=0,column=0,columnspan=3,sticky=(S,W,E,N),padx=5,pady=5)'''

#----------------------------------------------------------------------------------------------------------------------










#Window Resizing Magic
#----------------------------------------------------------------------------------------------------------------------
root.columnconfigure(0, weight=1,minsize=600)
root.rowconfigure(0, weight=1,minsize=600)

content.columnconfigure(0, weight=1)
content.rowconfigure(1, weight=1)

Body.columnconfigure(0, weight=1)
Body.rowconfigure(1, weight=1)
    
top_pane.columnconfigure(0, weight=1)
top_pane.columnconfigure(1, weight=1)

db_frame.columnconfigure(0,weight=1)
tb_frame.columnconfigure(0,weight=1)

records_tab.rowconfigure(0,weight=1)
records_tab.columnconfigure(0,weight=99)
records_tab.columnconfigure(1,weight=1)
records_tab.rowconfigure(1,weight=99)

recFrame.columnconfigure(0,weight=1)
recFrame.rowconfigure(0,weight=1)

'''tbEditFrame.columnconfigure(0,weight=1)
tbEditFrame.rowconfigure(0,weight=1)'''

#----------------------------------------------------------------------------------------------------------------------









#Menubar Magic
#----------------------------------------------------------------------------------------------------------------------
root.option_add('*tearOff',False)
menubarRoot = Menu(root)

optionMenu = Menu(menubarRoot)
feedbackMenu = Menu(menubarRoot)
helpMenu = Menu(menubarRoot)

menubarRoot.add_cascade(menu=optionMenu,label='Options')
menubarRoot.add_cascade(menu=feedbackMenu, label='Feedback')
menubarRoot.add_cascade(menu=helpMenu,label='Help')

optionMenu.add_command(label='Connect',command=conWinCall)
optionMenu.add_command(label='Developer Console',command=devWinCall)

feedbackMenu.add_command(label='Report Bug',command=bugRepWinCall)
feedbackMenu.add_command(label='Provide Feedback',command=feedWinCall)

helpMenu.add_command(label='GULAG Docs',command=docsWin)
helpMenu.add_command(label='Join help server (Discord)')
helpMenu.add_command(label='Request database root',command=dbrootreq)

root['menu']=menubarRoot
#----------------------------------------------------------------------------------------------------------------------

root.mainloop()
