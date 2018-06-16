import twitter
import datetime

from utils import get_env
from storage import save_friends, get_diff


consumer_key = get_env('consumer_key')
consumer_secret = get_env('consumer_secret')
access_token_key = get_env('access_token_key')
access_token_secret = get_env('access_token_secret')


api = twitter.Api(
    consumer_key=consumer_key, consumer_secret=consumer_secret,
    access_token_key=access_token_key, access_token_secret=access_token_secret)

users = api.GetFollowerIDs()
print(users)

today = datetime.date.today()
save_friends(today, users)

yesterday = today - datetime.timedelta(days=1)

unfollows, newfollows = get_diff(yesterday, today)

for u in unfollows:
    print(api.GetUser(u))
