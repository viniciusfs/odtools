#!/usr/bin/env python
# -*- coding: utf-8 -*-

# This file is part of ODtools project.
# (c) 2017, Vinicius Figueiredo <viniciusfs@gmail.com>

from fabric.api import local


def server():
    """Starts local development server."""
    local('python manage.py server')


def clean():
    """Clean project directory from temporary files."""
    local('find . -name \"*.pyc\" -exec rm {} \;')
    local('find . -name \"*.swp\" -exec rm {} \;')
    local('find . -name \"*~\" -exec rm {} \;')


def shell():
    """Starts a python shell inside application context."""
    local('python manage.py shell')
