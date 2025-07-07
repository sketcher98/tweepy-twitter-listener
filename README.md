# Tweepy Twitter Real-Time Listener

This project uses Tweepy to listen to tweets from a list of Twitter usernames in real time and sends new tweets to a webhook (like Make or Pipedream).

## 🔧 Setup

1. Create a `.env` file based on `.env.example`
2. Run `resolve_user_ids.py` to generate `user_ids.txt`
3. Deploy to Railway or run locally:

```
pip install -r requirements.txt
python index.py
```