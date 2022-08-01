import requests
from bs4 import BeautifulSoup

url = f"https://www.gelbeseiten.de/suche/{job}/{zipcode} {cityname}"
job = input()
zipcode = input()
cityname = input()