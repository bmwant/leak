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