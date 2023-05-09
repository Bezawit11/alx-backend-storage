#!/usr/bin/env python3
"""9-insert_school.py"""


def insert_school(mongo_collection, **kwargs):
    """inserts a new document in a collection based on kwargs"""
    for key, value in kwargs.items():
        r_id1 = mongo_collection.insert_one({key: value})
    return r_id1.inserted_id
