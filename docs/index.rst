.. Dota 2 CLI Companion documentation master file, created by
   sphinx-quickstart on Mon Jan 21 07:39:03 2019.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to Dota 2 CLI Companion's documentation!
================================================

Dota 2 CLI Companion is CLI application for quick finding of useful Dota informations.


Installation
------------

1. via test pypi_
	``python -m pip install --extra-index-url https://test.pypi.org/pypi dotacli``

2. manually
	- download the package from GitHub repository_
	- unpack it
	- run ``python setup.py install``


.. _pypi: https://test.pypi.org
.. _repository: https://github.com/klememi/dota-helper


Configuration file
------------------

The default path for configuration file is ``~/.dotacli``. If you want to specify custom path you can with ``-c/--config`` option.

Configuration contains two sections: *Favourite* and *Private*. Favourite section contains players IDs and Private section contains one key - *ID* - with value of your personal account ID.

This package contains example configuration file.


Usage
-----

- :ref:`usage`


Examples
--------

- :ref:`examples`


API
---

- :ref:`api`


License
-------

- :ref:`license`


.. toctree::
   :maxdepth: 2
   :hidden:
   :caption: Contents:

   usage
   examples
   api
   license


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
