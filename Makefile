install:
	poetry install

uninstall:
	pip uninstall hexlet-code -y

publish:
	poetry publish --dry-run

gendiff:
	poetry run gendiff

package-install:
	python3 -m pip install --user dist/*.whl --force

test:
	poetry run pytest

test-coverage:
	poetry run pytest --cov=gendiff --cov-report xml

lint:
	poetry run flake8 gendiff tests

selfcheck:
	poetry check

check: selfcheck test lint

build: check
	poetry build

.PHONY: install test lint selfcheck check build
