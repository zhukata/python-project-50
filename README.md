### Hexlet tests and linter status:
[![Actions Status](https://github.com/zhukata/python-project-50/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/zhukata/python-project-50/actions)
[![Maintainability](https://api.codeclimate.com/v1/badges/61a0c44599e1e7318b28/maintainability)](https://codeclimate.com/github/zhukata/python-project-50/maintainability)
[![Test Coverage](https://api.codeclimate.com/v1/badges/61a0c44599e1e7318b28/test_coverage)](https://codeclimate.com/github/zhukata/python-project-50/test_coverage)

# Gendiff: Configuration Files Comparison Tool

Description

Gendiff is a command line utility for comparing two configuration files. The tool analyzes the files and displays the differences in a human-readable format. It supports JSON and YAML file formats.
( Консольное приложение, позволяющее сравнить два файла в формате JSON или YAML и найти между ними отличия. )

## Installation

To install, clone the repository and install using `poetry`:

```sh
git clone https://github.com/Cur1yB/python-project-50
cd gendiff
poetry install
```

## Usage

To display usage information:

```sh
poetry run gendiff -h
```

Example of comparing two files:

```sh
poetry run gendiff filepath1.json filepath2.json
```

The output will appear in the following format:

```json
{
  - follow: false
    host: hexlet.io
  - proxy: 123.234.53.22
  - timeout: 50
  + timeout: 20
  + verbose: true
}
```

## Command Line Options

- `-h, --help` — display this help message and exit.
- `-f FORMAT, --format FORMAT` — set the output format (supported formats: `plain`, `json`, `stylish`).

## Output Formats

### Stylish

The default format. Shows changes in a tree structure.

### Plain

A flat text format, convenient for human reading:

```sh
Property 'common.follow' was added with value: false
```

### JSON

Outputs the changes in JSON format, convenient for machine processing.


Gendiff .json:
[![asciicast](https://asciinema.org/a/646480.svg)](https://asciinema.org/a/646480)

Gendiff .yaml:
[![asciicast](https://asciinema.org/a/648944.svg)](https://asciinema.org/a/648944)

Gendiff formater=stylish:
[![asciicast](https://asciinema.org/a/648946.svg)](https://asciinema.org/a/648946)

Gendiff formater=plain:
[![asciicast](https://asciinema.org/a/649321.svg)](https://asciinema.org/a/649321)

Gendiff formater=json_:
[![asciicast](https://asciinema.org/a/ybgC5efxgVNmm8MumyTEfixDQ.svg)](https://asciinema.org/a/ybgC5efxgVNmm8MumyTEfixDQ)
