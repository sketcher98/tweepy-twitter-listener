import tweepy
import os
import time

client = tweepy.Client(bearer_token=os.getenv("BEARER_TOKEN"))

usernames = open("usernames.txt").read().splitlines()
with open("user_ids.txt", "w") as f:
    for username in usernames:
        while True:
            try:
                user = client.get_user(username=username)
                user_id = user.data.id
                print(f"{username} => {user_id}")
                f.write(str(user_id) + "\n")
                time.sleep(2)  # delay between successful requests
                break  # break the retry loop if successful

            except tweepy.TooManyRequests as e:
                print("🚫 Rate limited! Waiting 15 minutes...")
                time.sleep(15 * 60)  # wait 15 mins

            except Exception as e:
                print(f"❌ Failed to get {username}: {e}")
                time.sleep(5)
                break  # skip to next username
