publish:
	@echo "Published"

test:
	@py.test -sv -rs tests

version-bump:
	@python bump_version.py