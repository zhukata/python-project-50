import pytest

import os

from gendiff.code.generate_diff import get_different


def get_fixture_path(file_name):
    current_dir = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(current_dir, 'fixtures', file_name)


def read(file_path):
    with open(file_path, 'r') as f:
        result = f.read()
    return result


dict1= {
    "host": "hexlet.io",
    "timeout": 50,
    "proxy": "123.234.53.22",
    "follow": False
  }

dict2 = {
    "timeout": 20,
    "verbose": True,
    "host": "hexlet.io"
  }


plain_data = read(get_fixture_path('plain.txt')).rstrip().split('\n\n\n')


def test_plain():
    assert get_different(dict1, dict2) == plain_data[0]