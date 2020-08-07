
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

'''
def createGulag():
    try:
        cursor.execute("CREATE DATABASE gulag")
        return 'Created Database'
    except mycon.Error as exc:
        return exc.msg


def createSampleTable():
    try:

        cursor.execute("CREATE TABLE sampletb(\
            uid INT(10),\
            uName VARCHAR(10),\
            uAdd VARCHAR(10),\
            uMail VARCHAR(10)\
            )")
        return "Created Table"
    except mycon.Error as exc:
        return exc.msg


def downloadDb():
    return

'''


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
            tbList.append(i)
        return tbList
    except mycon.Error as exc:
        return [exc.msg]

def returnTbdList(tName):
    try:
        tbdList=[]
        cursor.execute('desc '+tName) 
        for i in cursor:
            tbdList.append(i)
        return tbdList
    except mycon.Error as exc:
        return [exc.msg]



def crDB(name):
    try:
        cursor.execute('create database'+' '+name)
        tableCrCheck = returnTbList()
        if name in tableCrCheck:
            boolMsgClass.tf = True
            boolMsgClass.Msg = "Created"
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
        boolMsgClass.Msg = "Created Database "+name
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
        cursor.execute('truncate table'+' '+name)
        print("Successfully deleted all records from ",name)
    except:
        print('Error in executing command')

def deltab(name):
    try:
        cursor.execute('DROP table'+' '+name)
        print('Successfully deleted table ',name)
    except:
        print('Error in executing command')

def showall(tName):
    try:
        cursor.execute('SELECT * FROM '+tName)
        recList = []
        for i in cursor:
            recList.append(i)
        return recList
    except mycon.Error as e:
        return [e.msg]