## leak

[![PyPI](https://img.shields.io/pypi/v/leak?style=flat-square)](https://pypi.org/project/leak/)
[![PyPI - Downloads](https://img.shields.io/pypi/dm/leak?style=flat-square)](https://pepy.tech/project/leak)
[![PyPI - Wheel](https://img.shields.io/pypi/wheel/leak?style=flat-square)](https://pypi.org/project/leak/#files)
[![PyPI - License](https://img.shields.io/pypi/l/leak?style=flat-square)](https://tldrlegal.com/license/mit-license)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/leak?style=flat-square)](https://pypi.org/project/leak/)
[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)

[![Unittests](https://github.com/bmwant/leak/actions/workflows/unittests.yml/badge.svg)](https://github.com/bmwant/leak/actions/workflows/unittests.yml)

Show info about package releases on PyPI.

![screenshot](https://raw.githubusercontent.com/bmwant/leak/refs/heads/main/screenshot.png)

If you need to install specific version of package it is useful to know all available versions to have a choice.

Just run

```bash
leak <package_name>
# e.g.
leak pyramid
# show all available releases
leak django --all
```

and you will see releases and some useful statistic about package specified. It will show most recent version, most popular (with highest number of downloads) and some additional information.

### How to install

Install using pip

```bash
pip install leak

# or to make sure the proper interpreter is used
python -m pip install leak
```

or upgrade existing version

```bash
pip install --upgrade leak

# or with pip invoked as a module
python -m pip install --upgrade leak
leak --version
```

### Obtaining downloads data

It is possible to get downloads statistics for the target package by using third-party [pepy.tech](https://pepy.tech/) provider.
Create your own [API key](https://pepy.tech/pepy-api)(note that free one is a subject to some limitations) and configure it like shown below

```bash
# for the current shell session through the environment
export LEAK_API_KEY=<your_api_key>

# or store it within a configuration file
leak --set api-key=<your_api_key>
```

In case you are not interested in this data, and want to hide the warning displayed, run

```bash
leak --set show-downloads=false

# to enable it back once you have an api key
leak --set show-downloads=true
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
