import tweepy
# receive credentials from protected file.
# the protected file is not present on github
import x_credentials

# X Authentication initializer handler, needed to pass in the API
auth = tweepy.OAuth1UserHandler(x_credentials.api_key,
                                x_credentials.api_key_secret,
                                access_token=x_credentials.access_token,
                                access_token_secret=x_credentials.access_token_secret)
# The following is deprecated. Token are instead passed through the
# OAuth1userHandler initializer instead
# auth.set_access_token(access_token, access_token_secret)

# New syntax for X API 2.0, utilizing the client credentials above
new_api = tweepy.Client(bearer_token=x_credentials.bearer_token,
                        consumer_key=x_credentials.api_key,
                        consumer_secret=x_credentials.api_key_secret,
                        access_token=x_credentials.access_token,
                        access_token_secret=x_credentials.access_token_secret)

# Create the API passing the oauth handler as argument
api = tweepy.API(auth=auth)

# Pass the create_tweet result to a variable so you can view
# the server response later on
# Experiment later on with adding images or videos?! 2024/07/09
result = new_api.create_tweet(text="Even better way to tap into API 2.0... ")
print(result)
