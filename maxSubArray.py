# -*- coding:utf-8 -*-
__author__ = 'komorebi'

class MSA():
    """
    初始化nums的值
    """
    def __init__(self,num,array):
        self.num = num
        self.array = array
    """
    一维数组求最大子数组
    """
    def Calc(self):
        dp = []
        dp.append(self.array[0])
        for i in range(1, self.num):
            if dp[i - 1] < 0:
                dp.append(self.array[i])
            else:
                dp.append(self.array[i] + dp[i - 1])
        return max(dp)

    """
    二维数组求最大子数组
    """

if __name__ == '__main__':
    choice = int(input("功能：\n1、一维数组求最大子数组之和\n2、二维数组求最大子数组之和\n请选择："))