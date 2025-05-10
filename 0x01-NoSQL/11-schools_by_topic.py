#!/usr/bin/env python3
""" Module finds and retursn all schools with a specific topic """

def schools_by_topic(mongo_collection, topic):
    """ retusn the list of schools with a specific topic
    """
    return list(mongo_collection.find({ "topics": topic }))
