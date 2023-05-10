#!/usr/bin/env python3
""""REDIS"""


import redis
import uuid


class Cache:
    def __init__(self):
        _redis = redis.Redis()

    def store(self, data):
        a = uuid.uuid1()
        self._redis.set(a, data)
        return a

