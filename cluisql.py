import sqlcon

def sqlconect():
    try:
        sqlConClass = sqlcon.conect(h,u,p)
        if sqlConClass.con_bool:
            print("Connected")
            break
        else:
            print(sqlConClass.con_err)
    except Error as e:
        print(e)