import twitter
import datetime

from utils import get_env
from storage import save_friends, get_diff, save_result,\
    get_all_result_keys, get_by_key
from notification import send_notification


consumer_key = get_env('consumer_key')
consumer_secret = get_env('consumer_secret')
access_token_key = get_env('access_token_key')
access_token_secret = get_env('access_token_secret')


api = twitter.Api(
    consumer_key=consumer_key, consumer_secret=consumer_secret,
    access_token_key=access_token_key, access_token_secret=access_token_secret)

users = api.GetFollowerIDs()

today = datetime.date.today()
save_friends(today, users)

yesterday = today - datetime.timedelta(days=1)

unfollows, newfollows = get_diff(yesterday, today)

unfollows = map(lambda u: api.GetUser(u).screen_name, unfollows)
newfollows = map(lambda u: api.GetUser(u).screen_name, newfollows)

if get_by_key('result-%s' % today) != 'done':
    save_result(
        'result-%s' % today,
        ('unfollows:' +
         ','.join(unfollows) +
         '\n' + 'newfollows:' +
         ','.join(newfollows)))

result_keys = get_all_result_keys()
for k in result_keys:
    if get_by_key(k) != 'done':
        if send_notification(get_env('to_notify'), get_by_key(k)):
            save_result(k, 'done')
