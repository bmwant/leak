## leak

.. image:: https://img.shields.io/pypi/v/leak.svg
    :target: https://pypi.python.org/pypi/leak

.. image:: https://pepy.tech/badge/leak
    :target: https://pepy.tech/project/leak

.. image:: https://travis-ci.org/bmwant/leak.svg?branch=master
    :target: https://travis-ci.org/bmwant/leak

Show info about releases of packages on PyPi.

GitHub page `here <https://github.com/bmwant/leak>`_.

If you need to install specific version of package it is useful to know
all available versions to have a choice.

Just run

```bash
$ leak <package_name>
```

and you will see all releases and some useful statistic about package specified. It will show most recent version,
most popular (with highest number of downloads) and some additional information.

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
