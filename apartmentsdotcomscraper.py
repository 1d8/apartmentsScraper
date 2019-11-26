from bs4 import BeautifulSoup
from requests import get
headers = ({'User-Agent':
            'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36'})
city = input('Enter City: ').lower()
city = city.replace(' ', '-')
state = input('Enter State Abbreviation: ').lower()

for i in range(1,3):
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
        print("Name:", aptname, "\n", "Location:", addy, "\n", "Beds:", bedcount, "\n", "Price:", aptprice, "\n", "Phone Number:", phone, "\n")
        name.pop(0)
        location.pop(0)
        beds.pop(0)
        price.pop(0)
        contact.pop(0)
