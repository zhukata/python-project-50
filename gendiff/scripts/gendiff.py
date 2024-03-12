#!/usr/bin/env python3
from gendiff.code.generate_diff import generate_diff, parser


def main():
    generate_diff(parser())


if __name__ == '__main__':
    main()
