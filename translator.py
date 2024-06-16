import openai
import os
from dotenv import load_dotenv

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_twitter_post(title, content):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "system",
                "content": (
                "You are a Spanish writer David Kim that rewrites text in Castillian to make it more engaging. Ensure it is within 280 characters, "
                "focuses on SEO and avoids anti-plagiarism tools, and includes the keywords 'coreano en Barcelona' and 'Corea en Barcelona'. Ensure the message is crafted for Twitter, includes hashtags and is engaging."
                )
            },
            {
                "role": "user",
                "content": f"Rewrite the following article in Castillian Spanish for a Twitter post, keeping it within 280 characters and including appropriate hashtags:\n\nTitle: {title}\n\nContent: {content}"
            },
        ],
        max_tokens=280
    )
    tweet_content = response['choices'][0]['message']['content'].strip()
    return tweet_content
