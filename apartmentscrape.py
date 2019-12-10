#NOTE: THIS VERSION USES A DICTIONARY TO PRINT THE VALUES, PROVIDING A CLEANER OUTPUT COMPARED TO EXTRA.PY WHICH USES A BASIC PRINT STATEMENT
from bs4 import BeautifulSoup
from requests import get
import sys

headers = ({'User-Agent':
            'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36'})
city = input('Enter City: ').lower()
city = city.replace(' ', '-')
state = input('Enter State Abbreviation: ').lower()
print()
d = {}

for i in range(1,7):
    i = str(i)
    url = "https://apartments.com/" + city + "-" + state + "/" + i
    response = get(url, headers=headers)
    html_soup = BeautifulSoup(response.text, 'html.parser')
    name = html_soup.find_all('a', class_='placardTitle js-placardTitle')
    location = html_soup.find_all('div', class_='location')
    beds = html_soup.find_all('span', class_='unitLabel')
    price = html_soup.find_all('span', class_='altRentDisplay')
    contact = html_soup.find_all('div', class_='phone')
    
    for i in name:
        aptname = name[0]
        addy = location[0]
        bedcount = beds[0]
        aptprice = price[0]
        phone = contact[0]
        aptname = aptname.text
        addy = addy.text
        bedcount = bedcount.text
        aptprice = aptprice.text
        phone = phone.text
        phone = phone.replace('\n', '')
        aptname = aptname.replace('\r', '')
        aptname = aptname.replace('\n', '')
        d["Apartment Name:"] = aptname
        d["Address:"] = addy
        d["Beds:"] = bedcount
        d["Apartment Price:"] = aptprice
        d["Contact Number:"] = phone
        for key, value in d.items():
            print(key, value)
            try:
                name.pop(0)
                location.pop(0)
                beds.pop(0)
                price.pop(0)
                contact.pop(0)
            except IndexError:
                print('No More Listings Left')
                sys.exit()
        #print("Name:", aptname, "\n", "Location:", addy, "\n", "Beds:", bedcount, "\n", "Price:", aptprice, "\n", "Phone Number:", phone, "\n")


