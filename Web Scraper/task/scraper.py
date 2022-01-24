import requests

from bs4 import BeautifulSoup

print("Input the URL:")
url = input()
response = requests.get(url)
if response.status_code == 200:
    file = open('source.html', 'wb')

    file.write(response.content)
    file.close()
    print("Content saved.")
else:
    print(f"The URL returned {response.status_code}!")

