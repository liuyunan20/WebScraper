import requests

from bs4 import BeautifulSoup

num = input()
url = input()
r = requests.get(url)
soup = BeautifulSoup(r.content, "html.parser")
a = soup.find_all("a")
for i in a:
    if "act" + num in i.get("href", "no"):
        print(i.get("href"))
