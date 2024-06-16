import requests
from bs4 import BeautifulSoup

def scrape_latest_news():
    feed_url = "https://www.allkpop.com/rss_xml/sitemap1.xml"
    response = requests.get(feed_url)
    soup = BeautifulSoup(response.content, features="xml")

    news_list = []
    for item in soup.findAll("item")[:5]:  # Limit to 5 for simplicity
        news = {
            'title': item.title.text,
            'url': item.link.text,
            'image_url': item.enclosure['url'] if item.enclosure else '',
            'content': item.description.text
        }
        news_list.append(news)
    return news_list
