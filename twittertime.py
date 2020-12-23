import tweepy
import datetime

# Authenticate to Twitter
consumer_key = 'XXXXXXXXXXXXXXX'
consumer_secret = 'XXXXXXXXXXXXXXXXX'
access_token = 'XXXXXXXXXXXXXXXXX'
access_token_secret = 'XXXXXXXXXXXXXXXX'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

# Create API object
api = tweepy.API(auth)

tweettosend = ''

# Create a tweet
import datetime
def publictweet():
    if datetime.date.today().weekday() == 0:
        tweettosend = 'New week!! #TweetingFromABot'
    elif datetime.date.today().weekday() == 1:
        tweettosend = 'Tuesday is better than monday! #TweetingFromABot'
    elif datetime.date.today().weekday() == 2:
        tweettosend = 'Wednesday is better than Monday and Tuesday! #TweetingFromABot'
    elif datetime.date.today().weekday() == 3:
        tweettosend = 'Thursdays are kinda like fridays! #TweetingFromABot'
    elif datetime.date.today().weekday() == 4:
        tweettosend = 'Finally Friday!! #TweetingFromABot'
    elif datetime.date.today().weekday() == 5:
        tweettonsend = 'Great it is Saturday! College Football! #GoDucks #TweetingFromABot'
    elif datetime.date.today().weekday() == 6:
        tweettosend = 'Sunday morning, time to watch the Cowboys lose...again ): #TweetingFromABot'
    api.update_status(tweettosend)
    print(tweettosend)

# date and time tweet only one 'if', datetime and weekday, 0-6
print(datetime.date.today().weekday())

# post
publictweet()

