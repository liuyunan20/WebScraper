import requests

from bs4 import BeautifulSoup

print("Input the URL:")
url = input()
if "title" in url:
    response = requests.get(url, headers={'Accept-Language': 'en-US,en;q=0.5'})
    soup = BeautifulSoup(response.content, "html.parser")
    title = soup.find("h1")
    description = soup.find('span', {'data-testid': 'plot-xl'})
    t_d = {"title": title.text, "description": description.text}
    print(t_d)
else:
    print("Invalid movie page!")

