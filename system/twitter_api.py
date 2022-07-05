import tweepy
import pandas as pd


# Twitter API Credentials
api_key = 'nTCWFiz4JuIx1Z3BCty2EkmfY'
api_key_secret = 'KPmz8j7vR2H03W92rEPcBJpNh0tggeIYJNwmt9lHkU5HVO928H'
access_token = '1535967576311795717-OB6NeXWneM3atNlu9RqizXINQCWr5a'
access_token_secret = 'el8oFmSm3mofIkQ7AdviMJTM7hqZ2ZVcAdI7ocObbmLnA'

auth = tweepy.OAuthHandler(api_key, api_key_secret)
auth.set_access_token(access_token, access_token_secret)


# Twitter API
api = tweepy.API(auth)


# Get 10 latest tweets based on Twitter username
def tweetAnalyzer(username):
    username_df = []
    try:
        tweets = api.user_timeline(screen_name=username, count=100, exclude_replies=True, include_rts=False,
                                   tweet_mode='extended')
        for tweet in tweets[:10]:
            username_df.append({'Tweet': tweet.full_text})
        return pd.DataFrame.from_dict(username_df)

    except BaseException as e:
        print('User Not Found, ERROR', str(e))
        return pd.DataFrame()


