import tweepy
import pandas as pd

client = tweepy.Client("AAAAAAAAAAAAAAAAAAAAAC4yJQEAAAAARBS6H3umg2v9qAzC%2FbLCCHVAPQ4%3DUyuUY3g9TUwPeiw53AJFba4RGpqOqBG6zGBJCstWjY9ZiJ4YrN")
topics = ("amber heard", "trump", "crypto", "photography", "giveaway")
col_titles = ("amber_heard", "trump", "crypto", "photography", "giveaway")
d = {}
# with open("tweet-gathering/tweet-output.txt", "w", encoding="utf8") as f:

for topic, title in zip(topics, col_titles):
    max_iters = 8
    i = 0
    oldest_id = None
    tweets = []
    while i < max_iters:
        print("REQUESTING", f"{topic} -is:retweet -is:quote lang:en oldest id {oldest_id}")
        response = client.search_recent_tweets(f"{topic} -is:retweet -is:quote lang:en", until_id = oldest_id, max_results=100)
        if response.meta["result_count"] == 0: break
        oldest_id = response.meta["oldest_id"]
        
        for data in response.data:
            tweets.append(data.text)
            # f.write("###############\n")
            # f.write(data.text + "\n")
            # # print(data.text)
            # f.write("###############\n\n")
        i += 1
    
    d[title] = tweets

for val in d.values():
    print(len(val))
df = pd.DataFrame(data=d)
df.to_csv("tweet-gathering/week-dataset.csv", encoding="utf-8", index=False)
# with open("tweet-output.txt", "w", encoding="utf8") as f:
#     for i, data in enumerate(response.data):
#         f.write(f"{i} ###############\n")
#         f.write(data.text + "\n")
#         # print(data.text)
#         f.write("###############\n\n")

