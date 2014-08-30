# -*- coding: utf-8 -*-

import os
import unittest

from flask import Flask
from flaskext.versioned import Versioned, VersionedError

class VersionedTestCase(unittest.TestCase):

    def setUp(self):
        app = Flask(__name__)
        app.debug = False
        self.versioned = Versioned(app)
        self.app = app

    def tearDown(self):
        self.app = None
        self.versioned = None

    def test_00_existing_file_default_format(self):
        path = 'setup.py'
        versioned_path = self.versioned(path)
        assert versioned_path.startswith('/version-')
        assert versioned_path.endswith(path)

    def test_01_existing_file_custom_format(self):
        path = 'setup.py'
        v = Versioned(self.app, format='foo_%(version)s_%(path)s_bar')
        versioned_path = v(path)
        assert versioned_path.startswith('foo_')
        assert versioned_path.endswith('_bar')
        assert versioned_path.find('setup.py') != -1

    def test_02_nonexisting_file(self):
        path = 'nosuchfile'
        assert not os.path.isfile(path)
        self.assertRaises(VersionedError, self.versioned, path)

    def test_03_existing_dir(self):
        path = 'flaskext'
        assert os.path.isdir(path)
        self.assertRaises(VersionedError, self.versioned, path)

    def test_04_existing_file_root_relative(self):
        path = '/setup.py'
        versioned_path = self.versioned(path)
        assert versioned_path.startswith('/version-')
        assert versioned_path.endswith(path)
