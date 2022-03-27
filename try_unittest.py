# -*- coding: utf-8 -*-
__author__ = 'komorebi'

import unittest
from maxsubarray import MSA
from maxsubarray2D import MSA2D
from main import main

class Testing(unittest.TestCase):
    def test_main(self):
        self.assertEqual(main([]), 10)
        self.assertEqual(main([]), 10)
        self.assertEqual(main([]), 14)
        self.assertEqual(main([]), 14)
        self.assertEqual(main(['[1,2,3,4,-5,3]']),10)
        self.assertEqual(main(['[[1,-3,4],[2,3,-9],[1,5,8]]']),14)
        self.assertRaises(BaseException, main, '[1.2,5.22,-0.99]')
        self.assertRaises(BaseException, main, '[[[1,2],[2,3]],[[4,5],[6,7]]]')

    def test_maxsubarray(self):
        self.assertEqual(MSA(7, [1, -4, 2, 1, 5, -3, 8]).calc(), 13)
        self.assertRaises(BaseException, MSA(7, [1.90, -4.23, 2.32, 1.21, 5.55, -3.00, 8.11]).calc())
        self.assertRaises(BaseException, MSA(3, [[1, -3, 4], [2, 3, -9], [1, 5, 8]]))

    def test_maxsubarray2D(self):
        self.assertEqual(MSA2D(3,3,[[1,-3,4],[2,3,-9],[1,5,8]]).calc(),14)
        self.assertRaises(BaseException,MSA2D(3,3,[[1,12,-3.1,4.54],[2,3.76,-9.45],[1,5.43,8]]).calc())
        self.assertRaises(BaseException, MSA2D(3, 3, [1,4,5,-2,5,9]).calc())
        self.assertRaises(BaseException, MSA2D(3, 3, [[[1,2],[2,3]],[[4,5],[6,7]]]).calc())



if __name__ == "__main__":
    suite = unittest.TestSuite()

    tests = [Testing("test_main"),Testing("test_maxsubarray"),Testing("test_maxsubarray2D")]
    suite.addTests((tests))

    with open('./TestResult.txt','w') as file:
        runner = unittest.TextTestRunner(stream=file,verbosity=2)
        runner.run(suite)