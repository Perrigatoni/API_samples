import tweepy
# this works but looks messy... will try the solution by Medium:
# https://medium.com/@cn.april/posting-to-twitter-with-python-the-experience-and-code-fe62418e5af1


#removed outdated tokens


client = tweepy.Client(bearer_token,
                       api_key,
                       api_key_secret,
                       access_token,
                       access_token_secret)


def OAuth():
    try:
        auth = tweepy.OAuth1UserHandler(api_key,
                                        api_key_secret,
                                        access_token,
                                        access_token_secret)
        # api = tweepy.API(auth)
    except Exception as e:
        return e


client.create_tweet(text='Second sample tweet made from the API.')
print("Tweet created on X successfully!")


# DEPRECATED CODE, CANNOT WORK DUE TO API V2...

# def OAuth():
#     try:
#         # auth = tweepy.OAuthHandler(api_key, api_key_secret)
#         # auth.set_access_token(access_token, access_token_secret)
#         # input('Successfully authenticated')
#         # return auth
#         auth = tweepy.OAuth1UserHandler(consumer_key, consumer_key_secret,
#                                         access_token, access_token_secret)
#         input('Successfully authenticated')
#         return auth
#     except Exception:
#         return None


# api_call = tweepy.API(OAuth())

# api_call.update_status(
#     "Here is a sample tweet from the API call program.  Perrigatonious thangz!"
# )
# print("Tweet created.")
