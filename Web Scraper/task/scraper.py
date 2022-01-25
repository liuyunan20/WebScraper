import requests
import string
from bs4 import BeautifulSoup

url = "https://www.nature.com/nature/articles?sort=PubDate&year=2020&page=3"
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')
spans = soup.find_all('span', {'data-test': 'article.type'})
articles = []
for span in spans:
    # print(span.span.text)
    if span.span.text == "News":  # for every News type article:
        article = span.find_parent("article")  # find its <article> tag
        # find the <a> tag with hyperlink to this article
        a_link = article.find("a", {"data-track-action": "view article"})
        # translate the article title to underscores mode
        original_title = a_link.text
        table = original_title .maketrans(" ", "_", string.punctuation)
        a_title = original_title.translate(table) + ".txt"
        a_url = "https://www.nature.com" + a_link.get("href")  # the hyperlink to this article
        # get webpage content of this article
        a_response = requests.get(a_url)
        a_soup = BeautifulSoup(a_response.content, "html.parser")
        # find this article's body
        body = a_soup.find("div", {"class": "c-article-body u-clearfix"})
        file = open(a_title, "wb")
        print(body)
        file.write(body.text.encode())
        file.close()
        articles.append(a_title)
print(articles)
