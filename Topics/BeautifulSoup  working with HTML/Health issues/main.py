import requests

from bs4 import BeautifulSoup

letter = 'S'
url = input()
r = requests.get(url)
soup = BeautifulSoup(r.content, "html.parser")
a = soup.find_all("a")
topic_titles = []
for i in a:
    if ("entity" in i.get("href", "no") or "topics" in i.get("href", "no")) and len(i.text) > 1 and i.text.startswith(letter):
        topic_titles.append(i.text)
print(topic_titles)
