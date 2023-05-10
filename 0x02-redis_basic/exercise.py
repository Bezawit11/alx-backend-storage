#!/usr/bin/env python3
""""REDIS"""


import redis
import uuid


class Cache:
    def __init__(self):
        _redis = redis.Redis()

    def store(data):
        return uuid.uuid1()

