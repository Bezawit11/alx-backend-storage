#!/usr/bin/env python3
"""10-update_topics.py"""


def update_topics(mongo_collection, name, topics):
    """changes all topics of a school document based on the name"""
    myquery = {"name": name}
    new_values = {"$set": {"topics": topics}}
    mongo_collection.update_many(myquery, new_values)
