#!/usr/bin/env python3
""""REDIS"""


import redis
import requests


def get_page(url: str) -> str:
    """Implementing an expiring web cache and tracker""""

