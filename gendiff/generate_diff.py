import json
import yaml
from gendiff.formaters.stylish import stylish
from gendiff.formaters.plain import plain


def generate_diff(file_path1, file_path2, format_name='stylish'):
    diff = get_different(get_data(file_path1), get_data(file_path2))
    format = get_format(format_name)
    return format(diff)


def get_data(filepath):
    if check_format_file(filepath) == 'yaml':
        file_data = yaml.load(open(filepath), Loader=yaml.FullLoader)
    else:
        file_data = json.load(open(filepath))
    return file_data


def get_format(name_format):
    if name_format == 'plain':
        return plain
    return stylish


def check_format_file(filepath):
    if filepath.endswith('.yaml'):
        return 'yaml'
    elif filepath.endswith('.yml'):
        return 'yaml'
    elif filepath.endswith('.json'):
        return 'json'
    else:
        raise ValueError('unsupported file format')


def get_different(data1, data2):
    diff = {}
    keys_data1 = {key for key in data1.keys()}
    keys_data2 = {key for key in data2.keys()}
    set_keys = sorted(keys_data1 | keys_data2)
    index = 0
    for key in set_keys:
        index += 1
        if key not in data2:
            if isinstance(data1[key], dict):
                diff[index] = {
                    "key": key,
                    "status": "remowed",
                    "type": "nested",
                    "value": data1[key],
                }
                continue
            else:
                diff[index] = {
                    "key": key,
                    "status": "remowed",
                    "type": "plain",
                    "value": data1[key],
                }
                continue
        elif key not in data1:
            if isinstance(data2[key], dict):
                diff[index] = {
                    "key": key,
                    "status": "added",
                    "type": "nested",
                    "value": data2[key]
                }
                continue
            else:
                diff[index] = {
                    "key": key,
                    "status": "added",
                    "type": "plain",
                    "value": data2[key]
                }
                continue
        elif isinstance(data1[key], dict) and isinstance(data2[key], dict):
            diff[index] = {
                "key": key,
                "status": "equal",
                "type": "nested",
                "value": get_different(data1[key], data2[key]),
            }
            continue
        elif data1[key] == data2[key]:
            if isinstance(data1[key], dict):
                diff[index] = {
                    "key": key,
                    "status": "equal",
                    "type": "nested",
                    "value": data1[key],
                }
                continue
            else:
                diff[index] = {
                    "key": key,
                    "status": "equal",
                    "type": "plain",
                    "value": data1[key],
                }
                continue
        else:
            if isinstance(data1[key], dict) and not isinstance(data2[key], dict):
                diff[index] = {
                    "key": key,
                    "status": "updated",
                    "type1": "nested",
                    "type2": "plain",
                    "value1": data1[key],
                    "value2": data2[key]
                }
                continue
            if isinstance(data2[key], dict) and not isinstance(data1[key], dict):
                diff[index] = {
                    "key": key,
                    "status": "updated",
                    "type1": "plain",
                    "type2": "nested",
                    "value1": data1[key],
                    "value2": data2[key]
                }
                continue
            diff[index] = {
                "key": key,
                "status": "updated",
                "type1": "plain",
                "type2": "plain",
                "value1": data1[key],
                "value2": data2[key],
            }
    return diff
