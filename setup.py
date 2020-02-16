"""
py2app/py2exe build script for SpleeterGUI.

Usage (Mac OS X):
    python setup.py py2app

Usage (Windows):
    python setup.py py2exe
"""

import sys
from setuptools import setup

APP = ['spleeter_gui/SpleeterGUI.py']
DATA_FILES = ['spleeter_gui/main.qml']

if sys.platform == 'darwin':
    extra_options = {
        'setup_requires': ['py2app'],
        'app': APP,
        # Cross-platform applications generally expect sys.argv to
        # be used for opening files.
        'options': {'py2app': {'argv_emulation': True}},
    }
elif sys.platform == 'win32':
    extra_options = {
        'setup_requires': ['py2exe'],
        'app': APP,
    }
else:
    extra_options = {
        # Normally unix-like platforms will use "setup.py install"
        # and install the main script as such
        'scripts': APP,
    }

setup(
    name='SpleeterGUI',
    data_files=DATA_FILES,
    **extra_options
)
