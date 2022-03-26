# -*- coding: utf-8 -*-
__author__ = 'komorebi'

from maxsubarray import MSA

"""
扩展至二维，求最大的子矩阵的和
"""
class MSA2D():
    """
    初始化
    """
    def __init__(self,row,col,array):
        self.row = row
        self.col = col
        self.array = array
    

    """
    同样利用动态规划的思维计算二维矩阵的最大子矩阵的和
    """
    def Calc(self):
        theMax = self.array[0][0]
        for rowNumbers in range(1,self.row+1):
            for beginRow in range(self.row-rowNumbers+1):
                temp = []
                for count in range(self.col):
                    sum = 0
                    for i in range(rowNumbers):
                        sum += self.array[beginRow+i][count]
                    temp.append(sum)
                theMax = max(MSA(self.col,temp).Calc(),theMax)
        return theMax
