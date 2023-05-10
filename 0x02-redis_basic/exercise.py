#!/usr/bin/env python3
""""REDIS"""


import redis
import uuid
from typing import Union


class Cache:
    def __init__(self):
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]):
        a = str(uuid.uuid1())
        self._redis.set(a, data)
        return a

