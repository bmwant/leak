### Set up development environment

Clone repository (fork and clone your own repo for contributions) and install project with [Poetry](https://python-poetry.org/docs/)

```bash
$ git clone git@github.com:bmwant/leak.git
$ cd leak
$ poetry install
```

Set `LEAK_DEBUG` environment variable for the extra internal logging while developing

```bash
$ export LEAK_DEBUG=1
$ poetry run leak requests
```

### Testing

Unittests are written using [pytest](https://docs.pytest.org/en/latest/).

```bash
$ poetry run pytest -sv tests
# or
$ make tests
```

or to test on all possible environments

```bash
$ poetry run tox
```

### Releasing

Bump a version with features you want to include and build a package

```bash
$ poetry version patch  # patch version update
$ poetry version minor
$ poetry version major  # choose one based on semver rules
$ poetry build
```

Upload package to GitHub and PyPI

```bash
$ git tag -a 1.3.0 -m "Version 1.3.0"
$ git push --tags
$ poetry publish  # upload package to PyPI
```
