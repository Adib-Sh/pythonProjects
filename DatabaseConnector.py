import mysql.connector
import re
hostname = input('Please Enter your hostname:')
db = input('Which Database do you want to work on? ')
table = input('Which Table do you want to work on? ')
username = input('Please Enter your username:')
pw = input('Please Enter your Password:')
cnx = mysql.connector.connect(user=username, password=pw,
                              host=hostname,
                              database=db)

cursor = cnx.cursor()


stmt = "SHOW TABLES LIKE '%s'" %(table)
cursor.execute(stmt)
result = cursor.fetchone()
if result:
    pass
else:
    table_q = 'CREATE TABLE %s (email varchar(30), password varchar(30));'%(table)
    cursor.execute(table_q)


regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$' 
def check(email):

    if(re.search(regex, email)):
        return True 
    else:
       return False

email = input('Please Enter your E-mail:')

if check(email)==False:
    raise ValueError('Email adress is invalid. format: expression@string.string')
else:
    pass

pw = input('Please Enter your Password:')

add_creditionals = ("INSERT INTO creditionals "
               "(email,password) "
               "VALUES (%s, %s)")
data_creditionals = (email,pw)

cursor.execute(add_creditionals, data_creditionals)

cnx.commit()
cursor.close()
cnx.close()

    
    
