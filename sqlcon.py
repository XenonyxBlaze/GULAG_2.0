import mysql.connector as mycon

def con(p):
    try:
        global con
        con = mycon.connect(host='localhost', user = 'root' ,password = p)
        global cursor
        cursor = con.cursor()
        return True
    except:
        return False

def show():
    try:
        cursor.execute('show databases')
        for i in cursor:
            print(i)
    except:
        print('Error in executing the command')
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
