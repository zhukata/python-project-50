import json
import yaml

from gendiff.formaters.plain import plain
from gendiff.formaters.stylish import stylish
from gendiff.formaters.json_formatter import json_


def get_data(filepath):
    """Returns data from a file."""
    if get_format_file(filepath) == 'yaml':
        file_data = yaml.load(open(filepath), Loader=yaml.FullLoader)
    else:
        file_data = json.load(open(filepath))
    return file_data


def get_formatter(name_format):
    """Returns the formatter"""
    if name_format == 'plain':
        return plain
    elif name_format == 'json_':
        return json_
    return stylish


def get_format_file(filepath):
    """Returns the file format."""
    if filepath.endswith('.yaml'):
        return 'yaml'
    elif filepath.endswith('.yml'):
        return 'yaml'
    elif filepath.endswith('.json'):
        return 'json'
    else:
        raise ValueError('unsupported file format')
