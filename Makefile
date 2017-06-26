.PHONY: test clean release

test:
	@py.test -sv -rs tests

clean:
	rm -rf `find . -name __pycache__`
	rm -f `find . -type f -name '*.py[co]' `
	rm -f `find . -type f -name '*~' `
	rm -f `find . -type f -name '.*~' `
	rm -f `find . -type f -name '@*' `
	rm -f `find . -type f -name '#*#' `
	rm -f `find . -type f -name '*.orig' `
	rm -f `find . -type f -name '*.rej' `
	rm -f `find . -type f -name '.chunk_*'`
	rm -f `find . -type f -name 'tmp*'`
	rm -rf build/
	rm -rf dist/

release: clean
	python setup.py sdist
	python setup.py bdist_wheel
	twine upload -r pypi dist/*
