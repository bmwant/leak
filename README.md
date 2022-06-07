## leak

[![PyPI](https://img.shields.io/pypi/v/leak?style=flat-square)](https://pypi.org/project/leak/)
[![PyPI - Downloads](https://img.shields.io/pypi/dm/leak?style=flat-square)](https://pepy.tech/project/leak)
[![PyPI - Wheel](https://img.shields.io/pypi/wheel/leak?style=flat-square)](https://pypi.org/project/leak/#files)
[![PyPI - License](https://img.shields.io/pypi/l/leak?style=flat-square)](https://tldrlegal.com/license/mit-license)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/leak?style=flat-square)](https://pypi.org/project/leak/)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg?style=flat-square)](https://github.com/psf/black)

[![Unittests](https://github.com/bmwant/leak/actions/workflows/unittests.yml/badge.svg)](https://github.com/bmwant/leak/actions/workflows/unittests.yml)

Show info about package releases on PyPI.

![screenshot](https://github.com/bmwant/leak/blob/main/screenshot.png)

If you need to install specific version of package it is useful to know all available versions to have a choice.

Just run

```bash
$ leak <package_name>
# e.g.
$ leak pyramid
# show all available releases
$ leak django --all
```

and you will see releases and some useful statistic about package specified. It will show most recent version, most popular (with highest number of downloads) and some additional information.

### How to install

Install using pip

```bash
$ pip install leak

# or to make sure the proper interpreter is used
$ python -m pip install leak
```

or upgrade existing version

```bash
$ pip install --upgrade leak

# or with pip invoked as a module
$ python -m pip install --upgrade leak
$ leak --version
```

### Contribution

See [DEVELOP.md](https://github.com/bmwant/leak/blob/main/DEVELOP.md) to setup your local development environment and create pull request to this repository once new feature is ready.

### Releases

See [CHANGELOG.md](https://github.com/bmwant/leak/blob/main/CHANGELOG.md) for the new features included within each release.

### License

Distributed under [MIT License](https://tldrlegal.com/license/mit-license).

### Acknowledgement

🍋 [podmena](https://github.com/bmwant/podmena) for providing nice emoji icons to commit messages.

🐍 [PePy](https://pepy.tech/) for providing statistics about downloads.

🇺🇦 🇺🇦 🇺🇦 We would also thank the Armed Forces of Ukraine for providing security to perform this work. This work has become possible only because of resilience and courage of the Ukrainian Army.
