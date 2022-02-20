## leak

![PyPI](https://img.shields.io/pypi/v/leak?style=flat-square)
![PyPI - Downloads](https://img.shields.io/pypi/dm/leak?style=flat-square)
![PyPI - Wheel](https://img.shields.io/pypi/wheel/leak?style=flat-square)
![PyPI - License](https://img.shields.io/pypi/l/leak?style=flat-square)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

Show info about package releases on PyPI.

If you need to install specific version of package it is useful to know all available versions to have a choice.

Just run

```bash
$ leak <package_name>
# e.g.
$ leak pyramid
```

and you will see all releases and some useful statistic about package specified. It will show most recent version, most popular (with highest number of downloads) and some additional information.

### How to install

Install using pip

```bash
$ pip install leak

# or to make sure the proper interpreter is used
$ python -m pip install leak
```

or directly from github

```bash
$ git clone git://github.com/bmwant/leak.git
$ python setup.py install
```

### Contribution

See [DEVELOP.md](./DEVELOP.md) to setup your local development environment and create pull request to this repository once new feature is ready.

### License

Distributed under [MIT License](https://tldrlegal.com/license/mit-license).
