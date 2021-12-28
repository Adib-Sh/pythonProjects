import mysql.connector
hostname = input('Please Enter your hostname:')
db = input('Which Database do you want to work on? ')
table = input('Which Table do you want to work on? ')
username = input('Please Enter your username:')
pw = input('Please Enter your Password:')
cnx = mysql.connector.connect(user=username, password=pw,
                              host=hostname,
                              database=db)
cursor = cnx.cursor()

query = 'SELECT * FROM %s;'%(table)
cursor.execute(query)
newlst = []

for item in cursor:
    newlst.append(item)
      
sorted_newlst = sorted(newlst, key=lambda tup: (tup[2],-tup[1]),  reverse=True)
cnx.close()
for (name,weight,height) in sorted_newlst:
    print('%s %i %i' %(name,height,weight))