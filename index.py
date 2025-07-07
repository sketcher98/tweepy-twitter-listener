import os
import tweepy
import requests

BEARER_TOKEN = os.getenv("BEARER_TOKEN")
WEBHOOK_URL = os.getenv("WEBHOOK_URL")

class TweetListener(tweepy.StreamingClient):
    def on_tweet(self, tweet):
        print(f"📢 New tweet from {tweet.author_id}: {tweet.text[:80]}...")
        data = {
            "tweet_id": tweet.id,
            "author_id": tweet.author_id,
            "text": tweet.text,
        }
        try:
            res = requests.post(WEBHOOK_URL, json=data)
            print(f"✅ Webhook sent: {res.status_code}")
        except Exception as e:
            print("❌ Webhook error:", e)

# Start stream
if __name__ == "__main__":
    listener = TweetListener(BEARER_TOKEN)

    # Remove previous rules
    existing = listener.get_rules().data
    if existing:
        listener.delete_rules([r.id for r in existing])

    # Load user IDs from file
    with open("user_ids.txt", "r") as f:
        user_ids = [line.strip() for line in f if line.strip()]

    for uid in user_ids:
        listener.add_rules(tweepy.StreamRule(f"from:{uid}"))

    print("🚀 Listening for tweets...")
    listener.filter(tweet_fields=["author_id", "created_at"])