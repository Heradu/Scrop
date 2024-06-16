import tweepy
import os
from dotenv import load_dotenv

load_dotenv()

def create_api():
    consumer_key = os.getenv("TWITTER_API_KEY")
    consumer_secret = os.getenv("TWITTER_API_SECRET_KEY")
    access_token = os.getenv("TWITTER_ACCESS_TOKEN")
    access_token_secret = os.getenv("TWITTER_ACCESS_TOKEN_SECRET")

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    api = tweepy.API(auth)
    return api

def post_to_twitter(title, summary, image_url):
    api = create_api()
    tweet = f"{title}\n\n{summary}"
    
    filename = 'temp.jpg'
    request = requests.get(image_url, stream=True)
    if request.status_code == 200:
        with open(filename, 'wb') as image:
            for chunk in request:
                image.write(chunk)
        
        api.update_with_media(filename, status=tweet)
        os.remove(filename)
    else:
        api.update_status(status=tweet)
