import tweepy
import torch

client = tweepy.Client("AAAAAAAAAAAAAAAAAAAAAC4yJQEAAAAARBS6H3umg2v9qAzC%2FbLCCHVAPQ4%3DUyuUY3g9TUwPeiw53AJFba4RGpqOqBG6zGBJCstWjY9ZiJ4YrN")
# response = client.search_recent_tweets("amber heard -is:retweet -is:quote lang:en", until_id = None)
# print(response.meta)
# print(response.meta["oldest_id"])

# with open("tweet-output.txt", "w", encoding="utf8") as f:
#     for i, data in enumerate(response.data):
#         f.write(f"{i} ###############\n")
#         f.write(data.text + "\n")
#         # print(data.text)
#         f.write("###############\n\n")

bruh = torch.nn.Linear(120, 84)
print(bruh)
