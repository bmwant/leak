.PHONY: tests
tests:
	@poetry run pytest -sv tests

.PHONY: clean
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

.PHONY: release
release: clean
	@echo "Releasing"
