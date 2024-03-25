import pytest

import os

from gendiff.generate_diff import generate_diff


def get_fixture_path(file_name):
    current_dir = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(current_dir, 'fixtures', file_name)


def read(file_path):
    with open(file_path, 'r') as f:
        result = f.read()
    return result


@pytest.mark.parametrize("file_name1, file_name2, expected_result", [
    ["file1.json", "file2.json", "plain.txt"],
    ["file1.yaml", "file2.yml", "plain.txt"],
    ["file1.json", "file2.yml", "plain.txt"],
])
def test_generate_diff_plain(file_name1, file_name2, expected_result):
    with open(get_fixture_path(expected_result)) as file:
        assert generate_diff(get_fixture_path(file_name1), get_fixture_path(file_name2)) == file.read()


@pytest.mark.parametrize("file_name1, file_name2, expected_result", [
    ["file1_nested.json", "file2_nested.json", "nested.txt"],
    ["file1_nested.yml", "file2_nested.yaml", "nested.txt"],
    ["file1_nested.yml", "file2_nested.json", "nested.txt"]
])
def test_generate_diff_nested(file_name1, file_name2, expected_result):
    with open(get_fixture_path(expected_result)) as file:
        assert generate_diff(get_fixture_path(file_name1), get_fixture_path(file_name2)) == file.read()


def test_format():
    with pytest.raises(ValueError) as e:
        generate_diff(get_fixture_path("file1_nested.json"), get_fixture_path("file.txt"))

    assert str(e.value) == 'unsupported file format'