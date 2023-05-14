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
        k = method.__qualname__
        self._redis.rpush(inputs, str(args))
        o = method(self, *args, **kwargs)
        self._redis.rpush(outputs, str(o))
        return o
    return wrapper

def replay(method: Callable) - None:
    """"""
    local_redis = redis.Redis()
    n = local_redis.get(method.__qualname__).decode("utf-8")
    print("{} was called {} times:".format(method.__qualname__), n)
    inputs = local_redis.lrange("{}:inputs".format(method.__qualname__), 0, -1)
    outputs = local_redis.lrange("{}:outputs".format(method.__qualname__), 0, -1)
    for i, j in zip(inputs, outputs):
        print("{}(*{}) -> {}".format(method.__qualname__, i.decode("utf-8"), j.decode("utf-8")))

class Cache:
    def __init__(self):
        self._redis = redis.Redis()
        self._redis.flushdb()
        
    @count_calls
    @call_history
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
