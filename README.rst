url-shortener
=============

URL Shortener

Setup
-----

.. code-block:: bash

    $ pip install requirements.txt
    $ ./manage.py migrate
    $ ./manage.py createsuperuser

Local server
------------

.. code-block:: bash

    $ ./manage.py runserver --settings=url_shortener.settings.local

Production server
-----------------

.. code-block:: bash

    $ ./manage.py collectstatic
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

    $ ./manage.py shell

PostgreSQL interactive terminal 
-------------------------------

.. code-block:: bash

    $ ./manage.py dbshell
