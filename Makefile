.PHONY: run
run:
	python -m pycin

.PHONY: pep8
pep8:
	python -m pytest --pep8 pycin

.PHONY: tests
tests:
	python -m pytest pycin

.PHONY: tests-coverage
tests-coverage:
	python -m pytest --cov pycin

.PHONY: install-deps
install-deps:
	pip install -r requirements.txt
