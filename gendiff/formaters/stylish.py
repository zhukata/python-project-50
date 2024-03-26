INDENT = 4
SHIFT_LEFT = 2
DEPTH_STEP = 1


def stylish(data, replacer=' ', spaces_count=4, depth=DEPTH_STEP):
    diff = '{\n'

    deep_indent_size = depth * spaces_count
    left_shift = replacer * (deep_indent_size - SHIFT_LEFT)
    deep_indent = replacer * deep_indent_size
    current_indent = ((spaces_count * depth) - spaces_count) * replacer

    for key, change in data.items():
        if not isinstance(change, dict):
            diff += f"{deep_indent}{key}: {to_str(change)}\n"
            continue
        if change.get('status') == 'added':
            if change['type'] == 'nested':
                nested_changes = stylish(change['value'], depth=depth + DEPTH_STEP)
                diff += f"{left_shift}+ {change['key']}: {nested_changes}\n"
            else:
                diff += f"{left_shift}+ {change['key']}: {to_str(change['value'])}\n"
        elif change.get('status') == 'remowed':
            if change['type'] == 'nested':
                nested_changes = stylish(change['value'], depth=depth + DEPTH_STEP)
                diff += f"{left_shift}- {change['key']}: {nested_changes}\n"
            else:
                diff += f"{left_shift}- {change['key']}: {to_str(change['value'])}\n"
        elif change.get('status') == 'equal':
            if change['type'] == 'nested':
                nested_changes = stylish(change['value'], depth=depth + DEPTH_STEP)
                diff += f"{left_shift}  {change['key']}: {nested_changes}\n"
            else:
                diff += f"{left_shift}  {change['key']}: {to_str(change['value'])}\n"
        elif change.get('status') == 'updated':
            if change['type1'] == 'nested':
                nested_changes = stylish(change['value1'], depth=depth + DEPTH_STEP)
                diff += f"{left_shift}- {change['key']}: {nested_changes}\n"
            else:
                diff += f"{left_shift}- {change['key']}: {to_str(change['value1'])}\n"
            if change['type2'] == 'nested':
                nested_changes = stylish(change['value2'], depth=depth + DEPTH_STEP)
                diff += f"{left_shift}+ {change['key']}: {nested_changes}\n"
            else:
                diff += f"{left_shift}+ {change['key']}: {to_str(change['value2'])}\n"
        else:
            if isinstance(change, dict):
                nested_changes = stylish(change, depth=depth + DEPTH_STEP)
                diff += f"{left_shift}  {key}: {nested_changes}\n"
            else:
                diff += f"{deep_indent}  {key}:{to_str(change)}\n"
    diff += f"{current_indent}{'}'}"
    return diff


def to_str(value):
    if value is True or value is False:
        return str(value).lower()
    elif value is None:
        return 'null'
    return str(value)
