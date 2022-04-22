import tweepy as tw 
from time import sleep
from datetime import datetime
import json 

api_key = 'aysywmPajo3bv5ZWxtE24WiFO'
api_secret_key = '6pFf51Zu9CNe2AjcCmZDjZZo7qSqh0ow9mDyrd5AivfZXvN7lN'
client_id = 'SjFIX3Jxb0FRVUpyTDJtckFOTGc6MTpjaQ'
client_secret = 'wKTZlLp-uX2zP3jJdp-J74k54gR5pQigRG4tn83UajyKla8605'
bearer_token = 'AAAAAAAAAAAAAAAAAAAAAF%2FkbgEAAAAAuR1%2BB1D0s%2BxyrWfr73daYqWOwac%3DfhU7QWYYcSVXCQrmUozKBb6xboQKI4n6BLpfnJG1LGt4anobpw'
access_token = '1439283988473032710-FsV8cJeAOr6ybg1KaMctXodK860X5L'
access_secret_token = 'QdjWPwbnyWoIGoZF458UCZM76FWpDN14xXUTAwmdMD8iv'

auth = tw.OAuthHandler(client_id, client_secret)
auth.set_access_token(access_token, access_secret_token)

api = tw.API(auth)

public_tweets = api.home_timeline()

for tweet in public_tweets:
    print(tweet.text)
