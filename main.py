# !/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
main函数，程序入口
"""
__author__ = 'komorebi'

import sys
import traceback
import numpy as np

from maxsubarray import  MSA
from maxsubarray2D import MSA2D


def main(argv):
    """
    若通过命令行的方式运行程序，可在命令后面加入参数作为输入。
    若没有参数，则需要用户手动选择输入类型和输入内容。
    :param argv:
    :return:
    """
    if len(argv) == 0:
        test_choice = input("是否使用某个文件作为输入？(y/n)：")
        assert test_choice in ("y","n"),"请输入y或者n"
        if test_choice == "n":
            array_list = eval(input("请输入你的数组：\n"))
        elif test_choice == "y":
            file_path=input("请输入文件路径：")
            with open(file_path, mode='r', buffering=-1, encoding='utf-8') as fopen:
                array_list = eval(fopen.readline())
    elif len(argv) == 1:
        array_list = eval(argv[0])
    else:
        assert 0,"参数错误"
    array_numpy = np.array(array_list)
    dimension = len(array_numpy.shape)
    if dimension == 1:
        the_max = MSA(array_numpy.shape[0],array_list).calc()
        print("该一维数组其最大子数组之和为：{}".format(the_max))
    elif dimension == 2:
        the_max = MSA2D(array_numpy.shape[0],array_numpy.shape[1],array_list).calc()
        print("该二维矩阵其和最大的子矩阵和为：{}".format(the_max))
    else:
        assert 0,"请输入正确的一维或二维数组"

if __name__ == '__main__':
    try:
        main(sys.argv[1:])
    except KeyboardInterrupt:
        sys.exit(0)
    except OSError as err:
        print("OS error: {0}".format(err))
    except:
        traceback.print_exc()
