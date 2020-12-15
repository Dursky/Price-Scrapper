from bs4 import BeautifulSoup
import requests

#Example link
link = "https://www.olx.pl/elektronika/telefony-komorkowe/q-huawei-p10-lite/"

if(link ==""):
    print("nothing in link save")
    exit()

s = requests.get(link)
soup = BeautifulSoup(s.content, "lxml")

def average(list_to_do):
    a = sum(list_to_do)
    b = len(list_to_do)
    c = a /b
    return c

list_price = []
rows = soup.find_all("p", attrs={'class':'price'})
for row in rows:          
    #Some parse function 
    st_1 = row.get_text()[:-2]
    st_2 = st_1[:-1]
    st_3 = st_2.replace(" ","")
    integer = float(st_3.replace(',',''))
    list_price.append(integer)

print(average(list_price))#Print a result with average price
