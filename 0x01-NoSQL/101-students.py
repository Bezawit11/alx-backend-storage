#!/usr/bin/env python3
"""101-students.py"""


from pymongo import MongoClient


def top_students(mongo_collection):
    """returns all students sorted by average score"""
    a = mongo_collection.aggregate([
        { "$group": {
                "name": "$name",
                "averageScore": {"$avg": "$topics.score"}
            }
        },
        { "$sort": {"averageScore": -1}}
    ])
    return a
