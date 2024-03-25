import itertools


INDENT = 4
SHIFT_LEFT = 2
DEPTH_STEP = 1


def stylish(value, replacer=' ', spaces_count=4):

    def iter_(current_value, depth):

        deep_indent_size = depth * spaces_count
        left_shift = replacer * (deep_indent_size - 2)
        deep_indent = replacer * deep_indent_size
        current_indent = ((spaces_count * depth) - spaces_count) * replacer
        lines = []

        if isinstance(current_value, list):
            for i in current_value:
                if isinstance(i, dict):
                    if i['type'] == 'nested':
                        lines.append(f"{left_shift}  {i['key']}: {iter_(i['value'], depth + DEPTH_STEP)}") # noqa:501
                    elif isinstance(i['value'], dict):
                        lines.append(f"{left_shift}{i['type']} {i['key']}: {iter_(i['value'], depth + DEPTH_STEP)}") # noqa:501
                    else:
                        lines.append(f"{left_shift}{i['type']} {i['key']}: {to_str(i['value'])}") # noqa:501
        else:
            for k, v in current_value.items():
                if isinstance(v, dict):
                    lines.append(f"{deep_indent}{k}: {iter_(v, depth + 1)}")
                else:
                    lines.append(f"{deep_indent}{k}: {to_str(v)}")

        result = itertools.chain("{", lines, [current_indent + "}"])
        return '\n'.join(result)

    return iter_(value, 1)


def to_str(value):
    if value is True or value is False:
        return str(value).lower()
    elif value is None:
        return 'null'
    return str(value)
