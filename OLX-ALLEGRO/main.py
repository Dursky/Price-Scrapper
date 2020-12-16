from bs4 import BeautifulSoup
import requests

choose_platform = 0#Detect which one platform detect

#Example link for platforms
link = "https://www.ebay.pl/sch/15032/i.html?_from=R40&_nkw=iphone+12"

if any(x in link for x in ["ebay"]):
    print("------------------")
    print("Ebay:")
    choose_platform = 3
if any(x in link for x in ["allegro"]):
    print("------------------")
    print("Allegro:")
    choose_platform = 2
if any(x in link for x in ["olx"]):
    print("------------------")
    print("Olx:")
    choose_platform = 1


if(link ==""):
    print("nothing in link save - OLX")
    exit()

s = requests.get(link)
soup = BeautifulSoup(s.content, "lxml")

def average(list_to_do):
    a = sum(list_to_do)
    b = len(list_to_do)
    c = a /b
    return c

list_price = []
if(choose_platform == 1):
    rows = soup.find_all("p", attrs={'class':'price'})
if(choose_platform == 2):
    rows = soup.find_all("span", attrs={'class':'_1svub _lf05o'})
if(choose_platform ==3 ):
    rows = soup.find_all("span", attrs={'class':'ITALIC'})
for row in rows:          
    #Some parse function 
    st_1 = row.get_text()[:-2]
    st_2 = st_1[:-1]
    st_3 = st_2.replace(" ","")
    if(choose_platform == 1):
        floats = float(st_3.replace(',',''))
        list_price.append(floats)
    if(choose_platform == 2):
        st_4 = st_3[:-1]
        st_5 = st_4[:-1]
        res = st_5.replace(",","")
        floats = float(res)
        list_price.append(floats)
    if(choose_platform == 3):
        st_4 = st_3[:-1]
        st_5 = st_4[:-1]
        res = st_5.replace(",","")
        floats = float(res)
        list_price.append(floats)
    print(row.get_text())
#print(average(list_price))#Print a result with average price
print("------------------")