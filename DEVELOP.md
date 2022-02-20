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
