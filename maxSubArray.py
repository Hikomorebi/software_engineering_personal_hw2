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
    一维数组求最大子数组，使用动态规划
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