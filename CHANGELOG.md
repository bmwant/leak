### 2.3.0 🚜 ongoing work

## 2.2.1 📦 current package

* Fix displaying license name if full text is provided

## 2.2.0

* Fix obtaining downloads data for the package
* Allow storing settings in the configuration file

## 2.1.0

* Properly parse author/email/homepage/license from the fields available
* Use [pydantic-settings](https://docs.pydantic.dev/latest/concepts/pydantic_settings/) for configuration management

## 2.0.0

* Drop support for Python 3.7 and Python 3.8
* Migrate to Poetry 2.0
* Migrate to ruff for codestyle and linting
* Do not fail if downloads data is not available

## 1.6.0

* Add `--all` flag to show all versions available
* Add paginator if list of results is too long
* Adjust size of both panels
* Highlight homapage and email links

## 1.5.0

* Drop support for Python 3.6
* Use nice terminal UI for the output
* Add missing [packaging](https://github.com/pypa/packaging) library to the dependencies

## 1.4.0

* Migrate to click for the arguments parsing
* Integrate with GitHub Actions for CI
* Move configuration to a separate module
* Enable internal logging only in debug mode

## 1.3.0

* Use [rich library](https://rich.readthedocs.io/en/latest/) for the colored output
* Migrate to [Poetry](https://python-poetry.org/) for a package management
* Use [Markdown](https://www.markdownguide.org/basic-syntax/) for documentation files
* Apply formatting with [black](https://black.readthedocs.io/en/stable/index.html)
