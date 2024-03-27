#!/usr/bin/env python3
from gendiff.parser import parser
from gendiff.generate_diff import generate_diff


def main():
    return generate_diff(*parser())


if __name__ == '__main__':
    main()
