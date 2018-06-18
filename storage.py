import redis

from utils import get_env

r = redis.StrictRedis(
    host=get_env('redis_host', '127.0.0.1'),
    port=get_env('redis_port', 6379),
    db=get_env('redis_db', 0))


def save_friends(date, friends):
    for f in friends:
        r.sadd(date, f)


def get_diff(date1, date2):
    if r.scard(date1) == 0 or r.scard(date2) == 0:
        return [], []
    return r.sdiff(date1, date2), r.sdiff(date2, date1)


def save_result(date, result):
    r.set(date, result)


def get_all_result_keys():
    return r.keys('result-*')


def get_by_key(k):
    return r.get(k)
