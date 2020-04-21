=======================
Auto Deprecator Example
=======================

Auto deprecator example


* Free software: MIT license

The project is an example of using auto deprecator.

Installation
============

You just need a Python 3.x running in your machine.

Example
=======

To run all the deprecation examples

.. code-block:: console

  PYTHONWARNINGS=default::DeprecationWarning python test_deprecate_from_util.py

To run the automatic deprecation on the source codes, e.g. recursively in directory `auto_deprecator_example`

.. code-block:: console

  $ python auto_deprecator_example/utils/auto_deprecator.py auto_deprecator_example/ --version 2.0
  2020-04-21 17:37:57,544 Deprecating the file auto_deprecator_example/core.py
  2020-04-21 17:37:57,547 Deprecating the file auto_deprecator_example/__init__.py
  2020-04-21 17:37:57,548 Deprecating the file auto_deprecator_example/deprecate_from_utils/__init__.py
  2020-04-21 17:37:57,548 Deprecating the file auto_deprecator_example/deprecate_from_utils/func.py
  2020-04-21 17:37:57,549 Deprecating the file auto_deprecator_example/deprecate_from_utils/classes.py
  2020-04-21 17:37:57,552 Deprecating the file auto_deprecator_example/utils/__init__.py
  2020-04-21 17:37:57,552 Deprecating the file auto_deprecator_example/utils/auto_deprecator.py

The functions in the source codes are deprecated as they are expired regarding to the input current version (e.g. `--version 2.0`)

.. code-block:: console

  $ git status
  # On branch master
  # Changes not staged for commit:
  #   (use "git add <file>..." to update what will be committed)
  #   (use "git checkout -- <file>..." to discard changes in working directory)
  #
  #       modified:   auto_deprecator_example/deprecate_from_utils/classes.py
  #       modified:   auto_deprecator_example/deprecate_from_utils/func.py
  #

To update the auto deprecation package in the module `utils`

.. code-block:: console

  curl https://raw.githubusercontent.com/auto-deprecator/auto-deprecator/develop/auto_deprecator/__init__.py -o auto_deprecator_example/utils/auto_deprecator.py
