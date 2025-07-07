import os
import tweepy

API_KEY = os.getenv("API_KEY")
API_SECRET = os.getenv("API_SECRET")

client = tweepy.Client(bearer_token=os.getenv("BEARER_TOKEN"))

usernames = []
with open("usernames.txt", "r") as f:
    usernames = [line.strip() for line in f if line.strip()]

user_ids = []
for username in usernames:
    user = client.get_user(username=username)
    if user.data:
        uid = user.data.id
        print(f"{username} => {uid}")
        user_ids.append(str(uid))

with open("user_ids.txt", "w") as f:
    f.write("\n".join(user_ids))