# -*- coding:utf-8 -*-
"""
求一维数组最大子数组之和的类MSA()
"""
__author__ = 'komorebi'

class MSA():
    """
    使用动态规划算法计算最大子数组的和
    """
    def __init__(self,num,array):
        self.num = num
        self.array = array


    def calc(self):
        """
        一维数组求最大子数组，使用动态规划
        :return:
        """
        try:
            dp_list = []
            dp_list.append(self.array[0])
            for i in range(1, self.num):
                if dp_list[i - 1] < 0:
                    dp_list.append(self.array[i])
                else:
                    dp_list.append(self.array[i] + dp_list[i - 1])
            return max(dp_list)
        except:
            pass
