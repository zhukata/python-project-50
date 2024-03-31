def plain(data): # noqa:901
    """Formatter function. Shows flat format.
    Returns a string.
    """

    def iter_(current_value, path):
        lines = []
        for i in current_value:
            if path and not path.endswith('.'):
                path += '.'
            if isinstance(i, dict):
                if i.get('type') == 'nested':
                    lines.append(iter_(i['value'], path=path + i['key']))
                elif i.get('type') == 'added':
                    if isinstance(i['value'], dict):
                        lines.append(f"Property '{path + i['key']}' was added with value: [complex value]") # noqa:501
                    else:
                        lines.append(f"Property '{path + i['key']}' was added with value: {to_str(i['value'])}") # noqa:501
                elif i.get('type') == 'removed':
                    lines.append(f"Property '{path + i['key']}' was removed")
                elif i.get('type') == 'updated' and check_neighbour_type(i, current_value): # noqa:501
                    if isinstance(i['value'], dict) and isinstance(find_neighbour_value(i, current_value), dict): # noqa:501
                        lines.append(f"Property '{path + i['key']}' was updated. From [complex value] to [complex value]") # noqa:501
                    elif isinstance(i['value'], dict):
                        lines.append(f"Property '{path + i['key']}' was updated. From [complex value] to {to_str(find_neighbour_value(i, current_value))}") # noqa:501
                    elif isinstance(find_neighbour_value(i, current_value), dict): # noqa:501
                        lines.append(f"Property '{path + i['key']}' was updated. From {to_str(i['value'])} to [complex value]") # noqa:501
                    else:
                        lines.append(f"Property '{path + i['key']}' was updated. From {to_str(i['value'])} to {to_str(find_neighbour_value(i, current_value))}") # noqa:501

        return '\n'.join(lines)

    return iter_(data, '')


def to_str(value):
    """Converts the value to the desired format."""
    if value is True or value is False:
        return str(value).lower()
    elif value is None:
        return 'null'
    return f"'{str(value)}'"


def find_neighbour_value(elem, iter):
    """Returns the value of the next element in a sequence"""
    index = iter.index(elem)
    neighbour = iter[index + 1]
    value = neighbour.get('value')
    return value


def check_neighbour_type(elem, iter):
    """Check the type of the previous value in a sequence."""
    index = iter.index(elem)
    try:
        neighbour = iter[index + 1]
        type = neighbour.get('type') == 'updated'
    except IndexError:
        return False
    return type
