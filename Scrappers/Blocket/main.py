import requests
from bs4 import BeautifulSoup

start = 'https://www.blocket.se/annonser/hela_sverige/fordon/bilar?cg=1020&page='


carsli = []
i=1
for i in range(1,70):
    url = start + str(i)
    html = requests.get(url)
    soup = BeautifulSoup(html.text)
    cars  = soup.find_all('div', class_='styled__Wrapper-sc-1kpvi4z-0 ddgqIB')
    carsli.append(cars)

print(len(carsli))