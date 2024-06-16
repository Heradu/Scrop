import schedule
import time
from scraper import scrape_latest_news
from translator import translate_to_spanish
from summarizer import summarize_text
from twitter_client import post_to_twitter
from database import get_db, NewsArticle

def job():
    db = next(get_db())
    news_articles = scrape_latest_news()
    for article in news_articles:
        if db.query(NewsArticle).filter(NewsArticle.url == article['url']).first():
            continue
        
        translated_title = translate_to_spanish(article['title'])
        translated_content = translate_to_spanish(article['content'])
        summarized_content = summarize_text(translated_content)
        
        post_to_twitter(translated_title, summarized_content, article['image_url'])
        
        new_article = NewsArticle(
            title=article['title'], 
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
