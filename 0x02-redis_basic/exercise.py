#!/usr/bin/env python3
""""REDIS"""


import redis
import uuid
from typing import Union, Callable


class Cache:
    def __init__(self):
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]):
        a = str(uuid.uuid1())
        self._redis.set(a, data)
        return a

    def get(self, key, fn: Callable):
        return self_redis.get(key)

    def get_str(self, key):
        return self.get(key)
    
    def get_int(self, key):
        try:
            return int(self.get(key))
        except:
            return self.get(key)
