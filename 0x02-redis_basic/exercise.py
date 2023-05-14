#!/usr/bin/env python3
""""REDIS"""


import redis
import uuid
from typing import Union, Callable, Optional


def count_calls(fn: Callable) -> Callable:
    """count how many times methods of the Cache class are called"""
    def wrap(self, *args, **kwargs):
        k = fn.__qualname__
        self.incr(k)
        return fn(self, *args, **kwargs)
    return wrap




class Cache:
    def __init__(self):
        self._redis = redis.Redis()
        self._redis.flushdb()
        
    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        a = str(uuid.uuid1())
        self._redis.set(a, data)
        return a

    def get(self, key, fn: Optional[Callable] = None):
        v = self._redis.get(key)
        if not fn:
            return v
        else:
            return fn(v)

    def get_str(self, key):
        return self.get(key)
    
    def get_int(self, key):
        try:
            return int(self.get(key))
        except:
            return self.get(key)
