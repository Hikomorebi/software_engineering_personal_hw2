# -*- coding: utf-8 -*-

__author__ = 'komorebi'

import  pylint.lint


pylint_opts = ['./main.py']
pylint.lint.Run(pylint_opts)