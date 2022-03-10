# -*- coding:utf-8 -*-
__author__ = 'komorebi'

import maxSubArray

"""
扩展至二维，求最大的子矩阵的和
"""
class MSA2D():
    """
    初始化
    """
    def __init__(self,array,row,col):
        self.array = array
        self.row = row
        self.col = col

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
                theMax = max(maxSubArray.MSA(self.col,temp).Calc(),theMax)
        return theMax

if __name__ == '__main__':
    array = [[5,6,-3,8,-9,2],[1,-12,20,0,-3,-5],[0,-7,-3,6,7,-1]]
    print(MSA2D(array,3,6).Calc())