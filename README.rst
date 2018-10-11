leak
====

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

.. code:: bash

    leak <package_name>

and you will see all releases and some
useful statistic about package specified. It will show most recent version,
most popular (with highest number of downloads) and some additional
information.

How to install
--------------

Install using pip

.. code:: bash

    $ pip install leak

or directly from github

.. code:: bash

    $ git clone git://github.com/bmwant/leak.git
    $ python setup.py install

Testing
-------

Just invoke one of the possible commands, all of them use `pytest`.

.. code:: bash

    $ python setup.py test

or

.. code:: bash

    $ pytest

or

.. code:: bash

    $ make test

or to test on all possible environments

.. code:: bash

    $ tox

Releasing
---------

It uses `zestreleaser <https://zestreleaser.readthedocs.io/en/latest/>`_.
for versions management and `twine <https://twine.readthedocs.io/en/latest/>`_
for PyPI uploads.

.. code:: bash

    $ fullrelease
    $ make release

Contribution
------------

Create virtual environment and install all the necessary dependencies:

.. code:: bash

    $ pip install -e .[dev]

Then launch tests as described above and create a PR.

Licence
-------

Distributed under `MIT License <https://tldrlegal.com/license/mit-license>`_
