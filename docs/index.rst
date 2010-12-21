Flask-Versioned
===============

.. module:: flaskext.versioned

Installation
------------

Install the extension with one of the following commands::

    $ easy_install Flask-Versioned

or alternatively if you have pip installed::

    $ pip install Flask-Versioned


Set Up
------

Typical usage::

    from flask import Flask
    from flaskext.versioned import Versioned

    app = Flask(__name__)
    versioned = Versioned(app)

The default configuration will prefix last-modified timestamps to paths.

Versioning in Jinja Templates
-----------------------------

Example::

    <link rel="stylesheet" href="{{"static/css/style.css"|versioned}}">

Versioning in Python
--------------------

To rewrite paths in Python code, call the ``Versioned`` object::

    path = 'static/css/style.css'
    versioned_path = versioned(path)

Rewrite Rules and the Built-In Server
-------------------------------------

In production systems, you want to configure rewrite rules at the static files
server. Following is a hack to serve static files on a development server::

    @app.route('/version-<version>/<path:static_file>')
    def versioned_static(version, static_file):
        return redirect(static_file)

Custom Versioned Paths
---------------------------
The versioned path can be configured::

    from flask import Flask
    from flaskext.versioned import Versioned

    app = Flask(__name__)
    versioned = Versioned(app, format='/v%(version)s/%(path)s')

    # Returns '/v<timestamp>/static/favicon.ico'.
    versioned('static/favicon.ico')
