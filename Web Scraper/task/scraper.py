import requests
import string
from bs4 import BeautifulSoup
import os

page_num = int(input())
article_type = input()

for page in range(1, page_num + 1):
    os.mkdir(f"Page_{page}")
    url = f"https://www.nature.com/nature/articles?sort=PubDate&year=2020&page={page}"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    spans = soup.find_all('span', {'data-test': 'article.type'})
    articles = []
    for span in spans:
        # print(span.span.text)
        if span.span.text == article_type:  # for every News type article:
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
            file = open(f"Page_{page}/{a_title}", "wb")
            file.write(body.text.encode())
            file.close()
            articles.append(a_title)
    print(f"Page_{page} is saved")
