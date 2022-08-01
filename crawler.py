import requests
from bs4 import BeautifulSoup

job = input()
zipcode = input() #read from .csv file
cityname = input()
url = f"https://www.gelbeseiten.de/suche/{job}/{zipcode} {cityname}"
print(requests.get(url))