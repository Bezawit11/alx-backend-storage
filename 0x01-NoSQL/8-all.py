#!/usr/bin/env python3
"""8-all.py """


from pymongo import MongoClient


def list_all(mongo_collection):
    """lists all documents in a collection"""
    m = []
    cursor = mongo_collection.find({})
    for d in cursor:
        m.append(d)
    return m
