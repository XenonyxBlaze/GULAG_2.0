
import mysql.connector as mycon

class boolMsgClass:
    tf = bool(False)
    Msg = "Not Connected"

def connectSQL(h,u,p):
    try:

        global con
        con = mycon.connect(host=h, user = u,password = p)

        global cursor
        cursor = con.cursor()

        boolMsgClass.tf=True

        return boolMsgClass

    except mycon.Error as exc:

        boolMsgClass.tf=False
        boolMsgClass.Msg=exc.msg
        
        return boolMsgClass

def returnDbList():
    try:
        dbList=[]
        cursor.execute('show databases') 
        for i in cursor:
            dbList.append(i[0])
        return dbList
    except mycon.Error as e:
        return [e.msg]

def returnTbList():
    try:
        tbList=[]
        cursor.execute('show tables') 
        for i in cursor:
            tbList.append(i[0])
        return tbList
    except mycon.Error as exc:
        return [exc.msg]

def returnAllColList(tName):
    try:
        colList=[]
        cursor.execute('desc '+tName)
        for i in cursor:
            colList.append(i[0])
        return colList
    except mycon.Error as exc:
        return [exc.msg]

def crDB(name):
    try:
        cursor.execute('create database'+' '+name)
        databaseCrCheck = returnDbList()
        if name in databaseCrCheck:
            boolMsgClass.tf = True
            boolMsgClass.Msg = "Created Database "+name
            return boolMsgClass
        else:
            boolMsgClass.tf = False
            boolMsgClass.Msg = "Error"
            return boolMsgClass
    except mycon.Error as exc:
        boolMsgClass.tf = False
        boolMsgClass.Msg = exc.msg
        return boolMsgClass


def use(name):
    try:
        cursor.execute('use'+' '+name)
        return 'Now using database'+' '+name
    except mycon.Error as exc:
        return exc.msg


def dropDB(name):
    try:
        cursor.execute('drop database'+' '+name)
        boolMsgClass.tf = True
        boolMsgClass.Msg = "Deleted Database "+name
        return boolMsgClass
    except mycon.Error as exc:
        boolMsgClass.tf = False
        boolMsgClass.Msg = exc.msg
        return boolMsgClass

def crT(name):
    try:
        tb={}
        while True:
            c = input('Enter column name ')
            t = input('Enter column datatype ')
            s = input('Enter column size ')
            tb[c]=t+'('+s+')'
            print(tb)
            inp = input('enter Y to add another column // any key to create ')
            if inp.upper()=='Y':
                continue
            else:
                break
        tbc = ''
        li = list(tb.keys())
        for i in li[:-1]:
            tbc += i+' '+tb[i]+','
        tbc += li[-1]+' '+tb[i]
        print(tbc)
        print('create table'+' '+name+'('+tbc+')')
        cursor.execute('create table'+' '+name+'('+tbc+')')
        print('Successfully created table')
    except:
        print('Error in executing command')

def trun(name):
    try:
        cursor.execute('truncate table '+name)
        boolMsgClass.tf=True
        boolMsgClass.Msg='Successfully truncated table '+name
        return boolMsgClass
    except:
        boolMsgClass.tf=False
        boolMsgClass.msg=e.msg
        return boolMsgClass

def deltab(name):
    try:
        cursor.execute('DROP table '+name)
        boolMsgClass.tf=True
        boolMsgClass.Msg='Successfully deleted table '+name
        return boolMsgClass
    except mycon.Error as e:
        boolMsgClass.tf=False
        boolMsgClass.msg=e.msg
        return boolMsgClass

def showall(tName):
    try:
        cursor.execute('SELECT * FROM '+tName)
        recList = []
        for i in cursor:
            recList.append(i)
        return recList
    except mycon.Error as e:
        return [e.msg]

def givcommand(command):
    try:
        cursor.execute(str(command))
        boolMsgClass.tf=True
        li =[]
        for i in cursor:
            li.append(i)
        boolMsgClass.Msg=str(li)
        return boolMsgClass
    except mycon.Error as e:
        boolMsgClass.tf = False
        boolMsgClass.Msg = e.msg
        return boolMsgClass

def query(table,column,condition):
    try:
        cursor.execute('SELECT * FROM '+table+' WHERE '+column+' LIKE \'%'+condition+'%\'')
        li =[]
        for i in cursor:
            li.append(i)
        boolMsgClass.tf=True
        boolMsgClass.Msg=li
        return boolMsgClass
    except mycon.Error as e:
        boolMsgClass.tf = False
        boolMsgClass.Msg = e.msg
        return boolMsgClass

def addRecFunc(table,values):
    try:
        cursor.execute('Insert into '+table+' values('+values+')')
        boolMsgClass.tf=True
        boolMsgClass.Msg='Successfully added the record'
        return boolMsgClass
    except mycon.Error as e:
        boolMsgClass.tf = False
        boolMsgClass.Msg=e.msg
        return boolMsgClass