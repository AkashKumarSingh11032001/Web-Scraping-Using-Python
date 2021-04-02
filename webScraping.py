import requests
from bs4 import BeautifulSoup as bs

github_user = input("Enter github username: ")
url = 'https://github.com/'+github_user
# requesting server
req = requests.get(url)
# converting website to html
soup = bs(req.content, 'html.parser')
# selecting particular component from htlm
profile_image = soup.find('img',{'alt': 'Avatar'})['src']
# just printing image
print(profile_image)