# -*- coding: utf-8 -*-
__author__ = 'komorebi'

import  pylint.lint

file_list=['./main.py','./maxsubarray.py','./maxsubarray2D.py']
pylint_opts=['--rcfile=./pylint.conf','-ry']
for file in file_list:
    pylint_opts.append(file)
pylint.lint.Run(pylint_opts)