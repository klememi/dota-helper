Dota 2 Companion
================

|rtd|

.. |rtd| image:: https://readthedocs.org/projects/dota-cli/badge/?version=latest
    :target: https://dota-cli.readthedocs.io/en/latest/?badge=latest
    :alt: Documentation Status

Dota 2 Companion is Dota players' companion app built on OpenDota_ API. Written in Python running in CLI. Created as a semestral project at FIT CTU in Prague.

.. _OpenDota: https://opendota.com


Installation
------------

1. via test pypi_
    ``python -m pip install -i https://test.pypi.org/simple/ Dota-2-Companion``

2. manually
    - download the package from GitHub repository_
    - unpack it
    - run ``python setup.py install``

.. _pypi: https://test.pypi.org
.. _repository: https://github.com/klememi/dota-helper


Basic features
--------------

- List pro players details
- List pro matches details
- List public matches details
- Show distributions of MMR data by bracker and country
- Show top players by hero
- Show heroes details
- Show heroes in meta
- Find counter heroes
- List top currently ongoing live games
- Watch your favourite players' stats


Personal features
-----------------

You can add your Steam account ID to the configuration to access features based on you personal games.

- Show your personal stats
- Show your best heroes
- Find counter heroes based on your stats


Documentation
-------------

Please see full documentation on http://dota-cli.rtfd.io/ for more information.

Optionally you can build *docs* yourself.

1. install application (see `Installation`_)
2. run ``python -m pip install -r docs/requirements.txt``
3. ``make html`` in **docs** folder to generate html
4. ``make doctest`` in **docs** folder to test documentation

License
-------

**MIT**
