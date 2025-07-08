import tweepy
import os
import time

client = tweepy.Client(bearer_token=os.getenv("BEARER_TOKEN"))

usernames = open("usernames.txt").read().splitlines()
with open("user_ids.txt", "w") as f:
    for username in usernames:
        try:
            user = client.get_user(username=username)
            user_id = user.data.id
            print(f"{username} => {user_id}")
            f.write(str(user_id) + "\n")
            time.sleep(2)  # wait 2 seconds between requests
        except Exception as e:
            print(f"❌ Failed to get {username}: {e}")
            time.sleep(5)
