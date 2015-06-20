url-shortener
=============

URL Shortener

Setup
-----

.. code-block:: bash

    $ pip install requirements.txt
    $ ./manage.py migrate --settings=url_shortener.settings.local
    $ ./manage.py createsuperuser --settings=url_shortener.settings.local

Local server
------------

.. code-block:: bash

    $ ./manage.py runserver --settings=url_shortener.settings.local

Production server
-----------------

.. code-block:: bash

    $ honcho start

Test
-----

.. code-block:: bash

    $ ./manage.py test --settings=url_shortener.settings.test
    $ ./manage.py test --settings=url_shortener.settings.memory

Source code check
-----------------

.. code-block:: bash

    $ flake8 .

Interactive Python
------------------

.. code-block:: bash

    $ ./manage.py shell --settings=url_shortener.settings.local

PostgreSQL interactive terminal 
-------------------------------

.. code-block:: bash

    $ ./manage.py dbshell --settings=url_shortener.settings.local
