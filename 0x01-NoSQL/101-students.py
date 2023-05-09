#!/usr/bin/env python3
"""101-students.py"""


from pymongo import MongoClient


def top_students(mongo_collection):
    """returns all students sorted by average score"""
    m = []
    k = []
    d = {}
    s = 0
    a = 0
    for i in mongo_collection.find({}):
        d['name'] = i.get('name')
        for j in i.get('topics'):
            s += j['score']
            a += 1
        avg = s / a
        s = 0
        a = 0
        d['averagescore'] = avg
        m.append(d)
        d = {}
    return m
