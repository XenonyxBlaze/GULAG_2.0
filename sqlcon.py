
import mysql.connector as mycon

class conStatus:
    con_bool = bool(False)
    con_err = "Not Connected"

def conect(h,u,p):
    try:
        global con
        con = mycon.connect(host=h, user = u,password = p)
        global cursor
        cursor = con.cursor()
        conStatus.con_bool=True
        return conStatus
    except mycon.Error as exc:
        conStatus.con_bool=False
        conStatus.con_err=exc.msg
        return conStatus

def returnDbList():
    try:
        dbList=[]
        cursor.execute('show databases')
        for i in cursor:
            dbList.append(i[0])
        return dbList
    except mycon.Error as e:
        return e.msg

def create(name):
    try:
        cursor.execute('create database'+' '+name)
        print('database successfully created')
    except:
        print('Error in executing command')


def use(name):
    try:
        cursor.execute('use'+' '+name)
        print('Now using databse'+' '+name)
    except:
        print('Error in executing command')


def drop(name):
    try:
        cursor.execute('drop database'+' '+name)
        print('Successfully deleted database'+' '+name)
    except:
        print('Error in executing command')


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
