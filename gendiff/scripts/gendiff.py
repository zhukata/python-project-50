#!/usr/bin/env python3
from gendiff.parser import parser
# from gendiff.formaters.stylish import stylish
# # from gendiff.formaters.plain import plain
from gendiff.generate_diff import generate_diff


def main():
    return generate_diff(*parser())


if __name__ == '__main__':
    main()
