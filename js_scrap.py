import requests
from bs4 import BeautifulSoup


url = 'https://bitmesra.ac.in//'

data = requests.get(url)
soup = BeautifulSoup(data.text, 'html.parser')

print(soup.findAll('img'))
print(len(soup.findAll('img')))
