# -*- coding: utf-8 -*-
"""
求二维数组最大子矩阵和的类MSA2D
"""
__author__ = 'komorebi'

#import  numpy as np
from maxsubarray import MSA

class MSA2D():
    """
    扩展至二维，求最大的子矩阵的和
    """
    def __init__(self,row,col,array):
        self.row = row
        self.col = col
        self.array = array

    # def calc(self):
    #     """
    #     同样利用动态规划的思维计算二维矩阵的最大子矩阵的和:
    #     :return:
    #     """
    #     the_max = self.array[0][0]
    #     for row_numbers in range(1,self.row+1):
    #         for begin_row in range(self.row-row_numbers+1):
    #             temp = []
    #             for count in range(self.col):
    #                 temp.append(sum(np.array(self.array)[begin_row:begin_row+row_numbers,count]))
    #             the_max = max(MSA(self.col,temp).calc(),the_max)
    #     return the_max


    def calc(self):
        """
        同样利用动态规划的思维计算二维矩阵的最大子矩阵的和:
        :return:
        """
        try:
            assert isinstance(self.array[0], list)
            the_max = self.array[0][0]
            for row_numbers in range(1, self.row + 1):
                for begin_row in range(self.row - row_numbers + 1):
                    temp = []
                    for count in range(self.col):
                        the_sum = 0
                        for i in range(row_numbers):
                            the_sum += self.array[begin_row + i][count]
                        temp.append(the_sum)
                    the_max = max(MSA(self.col, temp).calc(), the_max)
            return the_max
        except:
            pass
