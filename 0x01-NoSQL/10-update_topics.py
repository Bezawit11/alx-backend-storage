#!/usr/bin/env python3
"""10-update_topics.py"""


def update_topics(mongo_collection, name, topics):
    """changes all topics of a school document based on the name"""
    m = []
    cursor = mongo_collection.find({})
    for d in cursor:
        m.append(d)
    for c in m:
        if c.get('name') == name:
            myquery = {c.get('name'): c.get('topics')}
            break
    newvalues = { "$set": {name: topics}}
    mongo_collection.update_one(myquery, newvalues)
