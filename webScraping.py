import requests
from bs4 import BeautifulSoup as bs

github_user = input("Enter github username: ")
url = 'https://github.com/'+github_user
req = requests.get(url)
