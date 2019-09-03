import urllib.request
from bs4 import BeautifulSoup


# url = "https://www.python.org/"
url = "https://www.politico.com/tipsheets/morning-money"
page = urllib.request.urlopen(url)
html_page = page.read()

soup_object = BeautifulSoup(html_page)

print(soup_object.title)
print(soup_object.title.text)

for link in soup_object.find_all('a'):
    print(link.get('href'))
