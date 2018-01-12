#!/usr/bin/env python
# -*- coding: utf-8 -*-

# This file is part of ODtools project.
# (c) 2017, Vinicius Figueiredo <viniciusfs@gmail.com>

from flask import current_app
from flask.ext.script import Manager, Server, Shell

from odtools.app import create_app


app = create_app()


def make_shell_context():
    return dict(app=current_app)


manager = Manager(app)
manager.add_command('server', Server)
manager.add_command('shell', Shell(make_context=make_shell_context))


if __name__ == '__main__':
    manager.run()
