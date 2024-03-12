import json
import argparse


def parser():
    parser = argparse.ArgumentParser(
        description="Compares two configuration files and shows a difference."
    )
    parser.add_argument("first_file")
    parser.add_argument("second_file")
    parser.add_argument("-f", "--format", help="set format of output")
    args = parser.parse_args()
    return args.first_file, args.second_file


def generate_diff(files):
    file1, file2 = files
    file1_data = json.load(open(file1))
    file2_data = json.load(open(file2))
    return print(get_different(file1_data, file2_data))


def get_different(data1, data2):
    result = ['{', '\n',]
    for key1, value1 in sorted(data1.items()):
        if key1 in data2:
            if data2[key1] == data1[key1]:
                result.append('  ')
                result.append(str(key1))
                result.append(':')
                result.append(' ')
                result.append(str(value1))
                result.append('\n')
            else:
                result.append('-')
                result.append(' ')
                result.append(str(key1))
                result.append(':')
                result.append(' ')
                result.append(str(value1))
                result.append('\n')
                result.append('+')
                result.append(' ')
                result.append(str(key1))
                result.append(':')
                result.append(' ')
                result.append(str(data2[key1]))
                result.append('\n')
        elif key1 not in data2:
            result.append('-')
            result.append(' ')
            result.append(str(key1))
            result.append(':')
            result.append(' ')
            result.append(str(value1))
            result.append('\n')
    for key2, value2 in sorted(data2.items()):
        if key2 not in data1:
            result.append('+')
            result.append(' ')
            result.append(str(key2))
            result.append(':')
            result.append(' ')
            result.append(str(value2))
            result.append('\n')
    result.append('}')
    return ''.join(result)
