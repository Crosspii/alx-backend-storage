#!/usr/bin/env python3
""" Module to list all documents in a mongodb collection."""

def list_all(mongo_collection):
    """ Lists all documents in the mongodb collection.
    """
    if mongo_collection is None:
        return []
    return list(mongo_collection.find())
