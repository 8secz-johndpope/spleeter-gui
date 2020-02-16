#!/usr/bin/env python

import PyInstaller.__main__

PyInstaller.__main__.run([
    '--name=SpleeterGUI',
    '--onefile',
    '--windowed',
    '--add-data=views:views',
    'main.py',
])
