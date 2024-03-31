import itertools


INDENT = 4
SHIFT_LEFT = 2
DEPTH_STEP = 1


def stylish(value, replacer=' ', spaces_count=4): # noqa:901
    """Formatter function. Describes changes to each key.
    Returns a string.
    """
    def iter_(current_value, depth):

        deep_indent_size = depth * spaces_count
        left_shift = replacer * (deep_indent_size - SHIFT_LEFT)
        deep_indent = replacer * deep_indent_size
        current_indent = ((spaces_count * depth) - spaces_count) * replacer
        lines = []

        if isinstance(current_value, list):
            for i in current_value:
                if isinstance(i, dict):
                    if i['type'] == 'nested':
                        lines.append(f"{left_shift}  {i['key']}: {iter_(i['value'], depth + DEPTH_STEP)}") # noqa:501
                    elif i['type'] == 'added':
                        if isinstance(i['value'], dict):
                            lines.append(f"{left_shift}+ {i['key']}: {iter_(i['value'], depth + DEPTH_STEP)}") # noqa:501
                        else:
                            lines.append(f"{left_shift}+ {i['key']}: {to_str(i['value'])}") # noqa:501
                    elif i['type'] == 'removed':
                        if isinstance(i['value'], dict):
                            lines.append(f"{left_shift}- {i['key']}: {iter_(i['value'], depth + DEPTH_STEP)}") # noqa:501
                        else:
                            lines.append(f"{left_shift}- {i['key']}: {to_str(i['value'])}") # noqa:501
                    elif i['type'] == 'equal':
                        if isinstance(i['value'], dict):
                            lines.append(f"{left_shift}  {i['key']}: {iter_(i['value'], depth + DEPTH_STEP)}") # noqa:501
                        else:
                            lines.append(f"{left_shift}  {i['key']}: {to_str(i['value'])}") # noqa:501
                    elif i['type'] == 'updated' and check_neighbour_type(i, current_value): # noqa:501
                        if isinstance(i['value'], dict):
                            lines.append(f"{left_shift}- {i['key']}: {iter_(i['value'], depth + DEPTH_STEP)}") # noqa:501
                        else:
                            lines.append(f"{left_shift}- {i['key']}: {to_str(i['value'])}") # noqa:501
                        if isinstance(find_neighbour_value(i, current_value), dict): # noqa:501
                            lines.append(f"{left_shift}+ {iter_(find_neighbour_value(i, current_value), depth + DEPTH_STEP)}") # noqa:501
                        else:
                            lines.append(f"{left_shift}+ {i['key']}: {to_str(find_neighbour_value(i, current_value))}") # noqa:501
        else:
            for k, v in current_value.items():
                if isinstance(v, dict):
                    lines.append(f"{deep_indent}{k}: {iter_(v, depth + DEPTH_STEP)}") # noqa:501
                else:
                    lines.append(f"{deep_indent}{k}: {to_str(v)}")

        result = itertools.chain("{", lines, [current_indent + "}"])
        return '\n'.join(result)

    return iter_(value, DEPTH_STEP)


def to_str(value):
    """Converts a value to a format json"""
    if value is True or value is False:
        return str(value).lower()
    elif value is None:
        return 'null'
    return str(value)


def check_neighbour_type(elem, iter):
    """Check the type of the previous value in a sequence."""
    index = iter.index(elem)
    try:
        neighbour = iter[index + 1]
        type = neighbour.get('type') == 'updated'
    except: # noqa:722
        return False
    return type


def find_neighbour_value(elem, iter):
    """Returns the value of the next element in a sequence"""
    index = iter.index(elem)
    neighbour = iter[index + 1]
    value = neighbour.get('value')
    return value
