#!/usr/bin/env python3
""""REDIS"""


import redis
import uuid


class Cache:
    def __init__(self):
        self._redis = redis.Redis()
        #_redis.flushdb()

    def store(self, data):
        a = str(uuid.uuid1())
        self._redis.set(a, data)
        return a

