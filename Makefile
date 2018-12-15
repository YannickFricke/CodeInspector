.PHONY: run \
		pep8 \
		tests \
		tests-coverage \
		install-deps

run:
	python -m pycin

pep8:
	python -m pytest --pep8 pycin

tests:
	python -m pytest pycin

tests-coverage:
	python -m pytest --cov pycin

install-deps:
	pip install -r requirements.txt
