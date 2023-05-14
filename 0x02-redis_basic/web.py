#!/usr/bin/env python3
""""REDIS"""


from functools import wraps
import redis
import requests
from typing import Union, Callable


r = redis.Redis()


def count_calls(method: Callable) -> Callable:
    """count how many times methods of the Cache class are called"""
    @wraps(method)
    def wrapper(url):
        """"increments value everytime the functin in called"""
        k = "count:{}".format(url)
        r.incr(k)
        v = r.get(k)
        if k:
            return str(v)
        else:
            r.setex(k, 10, method(url))
            return method(url)
    return wrapper

@count_calls
def get_page(url: str) -> str:
    """Implementing an expiring web cache and tracker""""
    x = requests.get(url)
    return x.text