#!/usr/bin/env python3
""""REDIS"""


import redis
import uuid
from typing import Union, Callable, Optional
from functools import wraps


def count_calls(method: Callable) -> Callable:
    """count how many times methods of the Cache class are called"""
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """"increments value everytime the functin in called"""
        k = method.__qualname__
        self._redis.incr(k)
        return method(self, *args, **kwargs)
    return wrapper


def call_history(method: Callable) -> Callable:
    """decorator to store the history of inputs and outputs of func"""
    inputs = method.__qualname__ + ":inputs"
    outputs = method.__qualname__ + ":outputs"

    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """äppends input and output list"""
        k = method.__qualname__
        self._redis.rpush(inputs, str(args))
        o = method(self, *args, **kwargs)
        self._redis.rpush(outputs, str(o))
        return o
    return wrapper


def replay(method: Callable) -> None:
    """display the history of calls of a particular function"""
    local_redis = redis.Redis()
    n = local_redis.get(method.__qualname__).decode("utf-8")
    m = method.__qualname__
    print("{} was called {} times:".format(m, n)
    inputs = local_redis.lrange("{}:inputs".format(m), 0, -1)
    outputs = local_redis.lrange("{}:outputs".format(m), 0, -1)
    for i, j in zip(inputs, outputs):
        print("{}(*{}) -> {}".format(m, i.decode("utf-8"), j.decode("utf-8")))


class Cache:
    """store an instance of the Redis client as a private variable
    named _redis (using redis.Redis()) and
    flush the instance using flushdb
    """
    def __init__(self):
        """Initialization"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    @call_history
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """stores key and value"""
        a = str(uuid.uuid1())
        self._redis.set(a, data)
        return a

    def get(self, key, fn: Optional[Callable] = None):
        """gets value of key"""
        v = self._redis.get(key)
        if not fn:
            return v
        else:
            return fn(v)

    def get_str(self, key):
        """"parametrizes"""
        return self.get(key)

    def get_int(self, key):
        """"parametrzes"""
        try:
            return int(self.get(key))
        except:
            return self.get(key)
