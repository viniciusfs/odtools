# -*- coding: utf-8 -*-

# This file is part of ODtools project.
# (c) 2017, Vinicius Figueiredo <viniciusfs@gmail.com>

from flask import Blueprint, render_template


admin = Blueprint('admin', __name__, url_prefix='/admin')

@admin.route('/')
def index():
  return render_template('admin/index.html')

