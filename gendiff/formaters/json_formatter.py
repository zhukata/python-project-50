import json


def json_(data):
    """Shows the complete difference between files as a json file"""
    return json.dumps(data, indent=2)
