#!/usr/bin/env python3
""""REDIS"""


import redis
import uuid
from typing import Union, Callable, Optional


class Cache:
    def __init__(self):
        self._redis = redis.Redis()
        self._redis.flushdb()

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
