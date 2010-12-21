# -*- coding: utf-8 -*-
"""
    flaskext.versioned
    ~~~~~~~~~~~~~~~~~~

    Rewrite file paths to add version info.

    :copyright: (c) 2010 by Simon Pantzare.
    :license: BSD, see LICENSE for more details
"""
import os
import time


__all__ = ['Driver', 'FileChangedDriver', 'Versioned']


class VersionedError(Exception):
    """Base error class."""
    pass


class Driver(object):
    def __init__(self, format='/version-%(version)s/%(path)s'):
        self.format = format

    def version(self, stream):
        raise NotImplementedError()


class FileChangedDriver(Driver):

    def version(self, stream):
        if not os.path.isfile(stream):
            raise VersionedError("no such file: %s" % stream)

        modt = time.localtime(os.path.getmtime(stream))
        mods = time.strftime('%Y%m%dT%H%M%S', modt)
        return self.format % {
            'version': mods,
            'path': stream,
        }


class Versioned(object):

    def __init__(self, app, driver_cls=FileChangedDriver, **driver_options):
        self._driver = driver_cls(**driver_options)
        app.jinja_env.filters.setdefault('versioned', self)

    def __call__(self, stream):
        return self._driver.version(stream)
