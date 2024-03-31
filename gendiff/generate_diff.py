from gendiff.data import get_data, get_formatter
from gendiff.get_different import get_different


def generate_diff(file_path1, file_path2, format_name='stylish'):
    diff = get_different(get_data(file_path1), get_data(file_path2))
    format = get_formatter(format_name)
    return format(diff)
