from bs4 import BeautifulSoup as bs
import requests
import mysql.connector

#Connection to DB

hostname = input('Please Enter your hostname:')
db = input('Which Database do you want to work on? ')
table = 'cars'
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
    table_q = 'CREATE TABLE %s (title varchar(30), millage varchar(30), price varchar(30));'%(table)
    cursor.execute(table_q)




#Scrapping data from truecar.com

baseurl = 'https://www.truecar.com'
make =input('Please enter your desired manufacturer:')
model =input('Please enter your desired model:')
web_url = requests.get('https://www.truecar.com/used-cars-for-sale/listings/%s/%s/?sort[]=created_date_desc'%(make,model))
soup = bs(web_url.text, 'html.parser')

car_lst = soup.find_all('a',{'linkable order-2 vehicle-card-overlay'})
linklst = []
for car in car_lst:
    link = car.get('href')
    linklst.append(baseurl+link)
linklst = linklst[0:20]    
data=[]
for link in linklst:
    f = requests.get(link).text
    hun=bs(f,'html.parser')
    try:
        title=hun.find("div",{'class':"heading-2"}).text.replace('\n',"")
    except:
      millage = 'No Info'
    try:
        price=hun.find("div",{'class':"heading-2 margin-top-3"}).text.replace('\n',"")
    except:
        price = 'No Price'
    try:
        millage=hun.find("p",{'class':"margin-top-1"}).text.replace('\n',"")
    except:
      millage = None
    car_details = {"title":title,"millage":millage,"price":price}

    data.append(car_details)    

#Inserting data to DB

add_details = ("INSERT INTO cars "
               "(title,millage,price) "
               "VALUES (%s, %s, %s)")

for i in range(0,len(data)):
    car_title = data[i]['title']
    car_millage = data[i]['millage']
    car_price = data[i]['price']
    data_details = (car_title,car_millage,car_price)
    cursor.execute(add_details, data_details)
    cnx.commit()

cursor.close()
cnx.close()


