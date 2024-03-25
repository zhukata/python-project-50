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
    list_diff = []
    keys_data1 = {key for key in data1.keys()}
    keys_data2 = {key for key in data2.keys()}
    set_keys = sorted(keys_data1 | keys_data2)
    for key in set_keys:
        if key not in data2:
            list_diff.append({
                "key": key,
                "type": '-',
                "value": data1[key],
            })
            continue
        elif key not in data1:
            list_diff.append({
                "key": key,
                "type": '+',
                "value": data2[key],
            })
            continue
        elif isinstance(data1[key], dict) and isinstance(data2[key], dict):
            list_diff.append({
                "key": key,
                "type": 'nested',
                "value": get_different(data1[key], data2[key])
            })
            continue
        elif data1[key] == data2[key]:
            list_diff.append({
                "key": key,
                "type": ' ',
                "value": data1[key],
            })
            continue
        else:
            list_diff.append({
                "key": key,
                "type": '-',
                "value": data1[key],
            })
            list_diff.append({
                "key": key,
                "type": '+',
                "value": data2[key]
            })
    return list_diff
