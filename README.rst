=================
Zish Python ANTLR
=================

A Python library for the `Zish format <https://github.com/tlocke/zish>`_ format,
released under the `MIT-0 licence <https://choosealicense.com/licenses/mit-0/>`_.

.. image:: https://github.com/tlocke/zish_python_antlr/workflows/zish_python_antlr/badge.svg
   :alt: Build Status

.. contents:: Table of Contents
   :depth: 2
   :local:


Installation
------------

- Create a virtual environment: ``python3 -m venv venv``
- Activate the virtual environment: ``source venv/bin/activate``
- Install: ``pip install zish_antlr``


Quickstart
----------

To go from a Python object to an Zish string use ``zish.dumps``. To go from a Zish
string to a Python object use ``zish.loads``. Eg.

>>> from zish import loads, dumps
>>> from datetime import datetime, timezone
>>> from decimal import Decimal
>>>
>>> # Take a Python object
>>> book = {
...     'title': 'A Hero of Our Time',
...     'read_date': datetime(2017, 7, 16, 14, 5, tzinfo=timezone.utc),
...     'would_recommend': True,
...     'description': None,
...     'number_of_novellas': 5,
...     'price': Decimal('7.99'),
...     'weight': 6.88,
...     'key': b'kshhgrl',
...     'tags': [
...       'russian',
...       'novel',
...       '19th century',
...     ],
... }
>>>
>>> # Output it as an Zish string
>>> zish_str = dumps(book)
>>> print(zish_str)
{
  "description": null,
  "key": 'a3NoaGdybA==',
  "number_of_novellas": 5,
  "price": 7.99,
  "read_date": 2017-07-16T14:05:00Z,
  "tags": [
    "russian",
    "novel",
    "19th century",
  ],
  "title": "A Hero of Our Time",
  "weight": 6.88,
  "would_recommend": true,
}
>>>
>>> # Load the Zish string, to give us back the Python object
>>> reloaded_book = loads(zish_str)
>>> 
>>> # Print the title
>>> print(reloaded_book['title'])
A Hero of Our Time


.. table:: Python To Zish Type Mapping

   +-----------------------+-----------------------------------------------------------+
   | Python Type           | Zish Type                                                 |
   +=======================+===========================================================+
   | bool                  | bool                                                      |
   +-----------------------+-----------------------------------------------------------+
   | int                   | integer                                                   |
   +-----------------------+-----------------------------------------------------------+
   | str                   | string                                                    |
   +-----------------------+-----------------------------------------------------------+
   | datetime.datetime     | timestamp                                                 |
   +-----------------------+-----------------------------------------------------------+
   | dict                  | map                                                       |
   +-----------------------+-----------------------------------------------------------+
   | decimal.Decimal       | decimal                                                   |
   +-----------------------+-----------------------------------------------------------+
   | float                 | decimal                                                   |
   +-----------------------+-----------------------------------------------------------+
   | bytearray             | bytes                                                     |
   +-----------------------+-----------------------------------------------------------+
   | bytes                 | bytes                                                     |
   +-----------------------+-----------------------------------------------------------+
   | list                  | list                                                      |
   +-----------------------+-----------------------------------------------------------+
   | tuple                 | list                                                      |
   +-----------------------+-----------------------------------------------------------+


Contributing
------------

Useful link:

* `ANTLR JavaDocs <http://www.antlr.org/api/Java/index.html?overview-summary.html>`_

To run the tests:

- Change to the ``zish_python_antlr`` directory: ``cd zish_python_antlr``
- Create a virtual environment: ``python3 -m venv venv``
- Activate the virtual environment: ``source venv/bin/activate``
- Install tox: ``pip install tox``
- Run tox: ``tox``

The core parser is created using `ANTLR <https://github.com/antlr/antlr4>`_ from the
Zish grammar. To create the parser files, go to the ``zish/antlr`` directory and
download the ANTLR jar and then run the following command:

``java -jar antlr-4.11.1-complete.jar -Dlanguage=Python3 Zish.g4``


Making A New Release
--------------------

* Run ``tox`` to make sure all tests pass
* Update the `Release Notes` section.
* Ensure ``build`` and ``twine`` are installed: ``pip install wheel twine``

Then do::

  git tag -a x.y.z -m "version x.y.z"
  rm -r dist
  python -m build
  twine upload --sign dist/*


Release Notes
-------------


Version 0.0.13 (2021-04-04)
```````````````````````````

- Trailing commas in list and maps are now allowed.


Version 0.0.12 (2017-09-07)
```````````````````````````

- Rename to `zish_antlr` to distinguish it from `zish`.


Version 0.0.11 (2017-09-07)
```````````````````````````

- Upload to PyPI failed for previous release.


Version 0.0.10 (2017-09-07)
```````````````````````````

- Allow lists and sets as keys to maps.


Version 0.0.9 (2017-08-24)
``````````````````````````

- Fix bug where ``int`` was being parsed as ``Decimal``.

- Make bytes type return a ``bytes`` rather than a ``bytearray``.


Version 0.0.8 (2017-08-24)
``````````````````````````

- Container types aren't allowed as map keys.

- Performance improvements.


Version 0.0.7 (2017-08-22)
``````````````````````````

- Fix bug with UTC timestamp formatting.


Version 0.0.6 (2017-08-22)
``````````````````````````

- Fix bug in timestamp formatting.

- Add note about comments.


Version 0.0.5 (2017-08-18)
``````````````````````````

- Fix bug where ``dumps`` fails for a ``tuple``.


Version 0.0.4 (2017-08-15)
``````````````````````````

- Simplify integer types.


Version 0.0.3 (2017-08-09)
``````````````````````````

- Fixed bug where interpreter couldn't find the ``zish.antlr`` package in eggs.

- Removed a few superfluous escape sequences.


Version 0.0.2 (2017-08-05)
``````````````````````````

- Now uses RFC3339 for timestamps.


Version 0.0.1 (2017-08-03)
``````````````````````````

- Fix bug where an EOF could cause an infinite loop.


Version 0.0.0 (2017-08-01)
``````````````````````````

- First public release. Passes all the tests.
