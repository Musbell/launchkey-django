virtualenv:
	virtualenv --distribute .env

install:
	pip install -e . --use-mirrors

install-test: install
	pip install "file://`pwd`#egg=launchkey_django[test]"

install-dev: install install-test
	pip install "file://`pwd`#egg=launchkey_django[dev]"

test: test-python

test-python:
	python setup.py -q test || exit 1

clean:
	rm -r .env/
