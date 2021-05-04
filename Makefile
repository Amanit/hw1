PACKAGES="src/hw1"

all: install black isort flake8 clean

black:
	@black ${PACKAGES}

isort:
	@isort ${PACKAGES}

flake8:
	@flake8 ${PACKAGES}

clean:
	@rm -rf `find . -name __pycache__`
	@rm -f `find . -type f -name '*.py[co]' `
	@rm -f `find . -type f -name '*~' `
	@rm -f `find . -type f -name '.*~' `
	@rm -f `find . -type f -name '@*' `
	@rm -f `find . -type f -name '#*#' `
	@rm -f `find . -type f -name '*.orig' `
	@rm -f `find . -type f -name '*.rej' `
	@rm -rf `find . -type d -name '.pytest_cache' `
	@rm -f .coverage
	@rm -rf htmlcov
	@rm -rf build
	@rm -rf cover
	@python setup.py clean
	@rm -rf .tox
	@rm -f .develop
	@rm -f .flake

install:
	@pip install -r requirements.txt

install-dev:
	@pip install -r requirements/dev.txt

install-test:
	@pip install -r requirements/test.txt
	@pip install -e .

install-all: install-dev install-test

pytest:
	@pytest

install-pre-commit: install-dev
	@pre-commit install

run-pre-commit:
	@pre-commit run --all-files
