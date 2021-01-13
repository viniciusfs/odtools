# -*- coding: utf-8 -*-

# This file is part of ODtools project.
# (c) 2017, Vinicius Figueiredo <viniciusfs@gmail.com>

from flask import Blueprint, redirect, url_for, render_template

main = Blueprint('main', __name__)


@main.route('/')
def index():
    return redirect(url_for('personagens.index'))

@main.route('/sobre')
def sobre():
    return render_template('main/sobre.html')
