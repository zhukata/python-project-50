import itertools


def plain(data):

    def iter_(current_value, path):
        lines = []
        for _, change in current_value.items():
            if path.endswith(change['key']):
                continue
            if path and not path.endswith('.'):
                path += '.'
            if change.get('status') == 'equal':
                if change['type'] == 'nested':
                    lines.append(iter_(change['value'], path=path + change['key']))
                else:
                    continue
            elif change.get('status') == 'added':
                if change['type'] == 'nested':
                    lines.append(f"Property '{path + change['key']}' was added with value: [complex value]")
                else:
                    lines.append(f"Property '{path + change['key']}' was added with value: {to_str(change['value'])}")
            elif change.get('status') == 'remowed':
                lines.append(f"Property '{path + change['key']}' was removed")
            elif change.get('status') == 'updated':
                if change['type1'] == 'nested' and change['type2'] == 'nested':
                    lines.append(f"Property '{path + change['key']}' was updated. From [complex value] to [complex value]")
                elif change['type1'] == 'nested':
                    lines.append(f"Property '{path + change['key']}' was updated. From [complex value] to {to_str(change['value2'])}")
                elif change['type2'] == 'nested':
                    lines.append(f"Property '{path + change['key']}' was updated. From {to_str(change['value1'])} to [complex value]")
                else:
                    lines.append(f"Property '{path + change['key']}' was updated. From {to_str(change['value1'])} to {to_str(change['value2'])}")

        result = itertools.chain(lines)
        return '\n'.join(result)

    return iter_(data, '')


def to_str(value):
    if value is True or value is False:
        return str(value).lower()
    elif value is None:
        return 'null'
    return f"'{str(value)}'"
