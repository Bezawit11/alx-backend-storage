#!/usr/bin/env python3
""""REDIS"""


import redis
import uuid


class Cache:
    def __init__(self):
        _redis = redis.Redis()

    def store(self, data):
        self._redis.set(uuid.uuid1(), data)
        return self._redis 

