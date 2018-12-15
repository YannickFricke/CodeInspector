.PHONY: run \
		tests \
		install-deps

run:
	python main.py

pep8:
	python -m pytest --pep8

tests:
	python -m pytest tests/

tests-coverage:
	python -m pytest --cov tests/

install-deps:
	pip3 install -r requirements.txt
