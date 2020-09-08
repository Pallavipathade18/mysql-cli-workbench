import mysql.connector

def connectToDB(dbname,password):
    user="root"
    host="localhost"
    password="root"

    conn=mysql.connector.connect(user=user,host=host,password=password,database="employee")
    return conn

def ShowTables(conn):
    show ='SHOW TABLES'
    cursor = conn.cursor()
    cursor.execute(show)
    result=cursor.fetchall()
    return result

def SelectFromTable(tablename,conn,attr):
    if len(attr)==0:
        users = 'SELECT * FROM ' + tablename
    else:
        users = 'SELECT '
        for i in range(len(attr)):
            if(i<len(attr)-1):
                 users+=attr[i]
                 users+=','
            else:
                users+=attr[i]
        users+='FROM'+tablename

    cursor = conn.cursor()
    cursor.execute(users)
    result= cursor.fetchall()
    for i in result:
        print(i)

def UpdateTable(attr,tablename,where,key,conn):
    update='UPDATE '+tablename+' SET '
    if(len(attr)>0):
        j=0
        for i in attr:
            if(j<len(attr)-1):
                update+=i
                update+=' = "'
                update+=attr[i]
                update+='" , '
            else:
                update+=i
                update+=' = "'
                update+=attr[i]
                update+='" '
            j+=1
    update+='WHERE '
    if(len(where)>0):
        j=0
        for i in where:
            if(j<len(where)-1):
                update+='"'+i+'"'
                update+=' = "'
                update+=where[i]
                update+=' '+key+' '
            else:
                update+='"'+i+'"'
                update+=' = "'
                update+=where[i]
                update+='" '
            j+=1
    print(update)
    cursor = conn.cursor()
    cursor.execute(update)
    conn.commit()

def DeleteTable(tablename,attr,value,conn):
    delete = 'DELETE FROM '+tablename+' WHERE '+attr+'="'+value+'"'
    print(delete)
    cursor = conn.cursor()
    cursor.execute(delete)
    conn.commit()


conn = connectToDB('employee','')


SelectFromTable('employee',conn,[])
d={'Id':'400',
'Addr':'Chennai'}
w={'Age':'29'}
UpdateTable(d,'employee',w,'and',conn)
DeleteTable('employee','Salary',"30000",conn)
SelectFromTable('employee',conn,[])