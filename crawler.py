import requests
from bs4 import BeautifulSoup

job = input("Insert Job here: ")
zipcode = int(input("Insert Zipcode here: ")) #read from .csv file
cityname = input("Input city here: ") #read from .csv file
url = f"https://www.gelbeseiten.de/suche/{job}/{zipcode} {cityname}"
print(requests.get(url))