import schedule
import time
from scraper import scrape_latest_news
from translator import generate_twitter_post  # Updated function name
from twitter_client import post_to_twitter
from database import get_db, NewsArticle

def job():
    db = next(get_db())
    news_articles = scrape_latest_news()
    for article in news_articles:
        if db.query(NewsArticle).filter(NewsArticle.url == article['url']).first():
            continue
        
        twitter_post = generate_twitter_post(article['title'], article['content'])
        
        post_to_twitter(twitter_post, article['image_url'])
        
        new_article = NewsArticle(
            title=article['title'],  # We still keep the title for reference in the database
            url=article['url'], 
            image_url=article['image_url']
        )
        db.add(new_article)
        db.commit()

if __name__ == "__main__":
    schedule.every(60).minutes.do(job)
    
    while True:
        schedule.run_pending()
        time.sleep(1)
