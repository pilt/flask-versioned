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
    def __init__(self, app, format='/version-%(version)s/%(path)s'):
        self.app = app
        self.format = format

    def version(self, stream):
        raise NotImplementedError()


class FileChangedDriver(Driver):

    def version(self, stream):
        path = stream
        if os.path.isabs(path):
            pass
        else:
            path = os.path.join(self.app.root_path, path)

        if not os.path.isfile(path):
            raise VersionedError("no such file: %s" % path)

        modt = time.localtime(os.path.getmtime(path))
        mods = time.strftime('%Y%m%dT%H%M%S', modt)
        return self.format % {
            'version': mods,
            'path': stream,
        }


class Versioned(object):

    def __init__(self, app, driver_cls=FileChangedDriver, **driver_options):
        self._driver = driver_cls(app, **driver_options)
        app.jinja_env.filters.setdefault('versioned', self)

    def __call__(self, stream):
        return self._driver.version(stream)
