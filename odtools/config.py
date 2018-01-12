# -*- coding: utf-8 -*-

# This file is part of ODtools project.
# (c) 2017, Vinicius Figueiredo <viniciusfs@gmail.com>

import os


class BaseConfig(object):
    ROOT_DIR = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
    LOG_DIR = os.path.join(ROOT_DIR, 'log')
    DATA_DIR = os.path.join(ROOT_DIR, 'data')
    TMP_DIR = os.path.join(ROOT_DIR, 'tmp')

    DEBUG = False


class DefaultConfig(BaseConfig):
    DEBUG = True
