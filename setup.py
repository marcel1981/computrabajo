#!/usr/bin/env python
# -*- coding: utf-8 -*-

from distutils.core import setup

setup(
    name='computrabajo',
    version='0.2dev',
    author='Mario Rodas',
    author_email='rodasmario2@gmail.com',
    packages=['computrabajo'],
    license='MIT License',
    description= 'pseudo-api for computrabajo.com',
    long_description=open('README.rst').read(),
    install_requires=[
        'BeautifulSoup4',
    ],
)

