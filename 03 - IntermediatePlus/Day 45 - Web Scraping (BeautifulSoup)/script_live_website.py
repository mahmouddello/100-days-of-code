import requests
from bs4 import BeautifulSoup

response = requests.get("https://news.ycombinator.com/news")  # random article

yc_page = response.text  # response as html

soup = BeautifulSoup(yc_page, "html.parser")
print(soup.prettify())
print("*" * 50)
# yc_page title

article_tag = soup.select_one(".titleline a")
article_text = article_tag.get_text()  # text of the article
article_link = article_tag.get('href')
article_upvote = soup.find(name='span', class_="score")
print(f"{article_text}\nUpvote: {article_upvote.get_text()}\nLink: {article_link}")

print("-" * 50)
articles = soup.select(".title .titleline a")
articles_text = [article_tag.get_text() for article_tag in articles]
print(articles_text)
articles_links = [article_tag.get("href") for article_tag in articles]
print(articles_links)
