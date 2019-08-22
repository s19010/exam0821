import requests
from bs4 import BeautifulSoup

r = requests.get("https://パワプロ.gamewith.jp/article/show/10913")
soup = BeautifulSoup(r.text, "html.parser")

file = open('pawapuro.txt', 'w')

for i in soup.select("tr"):
    file.write(i.getText() + '\n')

file.close()
