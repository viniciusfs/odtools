# -*- coding: utf-8 -*-

# This file is part of ODtools project.
# (c) 2017, Vinicius Figueiredo <viniciusfs@gmail.com>

from flask import Blueprint, render_template

main = Blueprint('main', __name__)


@main.route('/')
def index():
    return render_template('main/index.html')

@main.route('/sobre')
def sobre():
    return render_template('main/sobre.html')
