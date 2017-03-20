from unittest import TestCase
from ..functions import getDiffOfMean, getMeanDiffListForAllPermutations\
                      , getDiffOfMeanRandomized
import numpy as np

class TestGetDiffOfMean(TestCase):
    def test_calculation(self):
        
        lst_1 = [1,2,3]
        lst_2 = [4,5,6]
        res = getDiffOfMean(lst_1, lst_2)
        self.assertEqual(-3, res)

    def test_calculation(self):
        
        lst_1 = [1,2,3]
        lst_2 = [4,5,6]

        res = getDiffOfMean(lst_1, lst_2)
        self.assertEqual(-3, res)    


    def test_nan_input(self):
        #nans should be ignored
        lst_1 = [1,2,3, np.nan]
        lst_2 = [4,5,6]

        res = getDiffOfMean(lst_1, lst_2)
        self.assertEqual(-3, res)    

    def test_none_output(self):
        lst_1 = [np.nan, np.nan]
        lst_2 = [4,5,6]
        self.assertRaises(ValueError, getDiffOfMean, lst_1, lst_2)    

    def test_single_elements(self):
        #should work with singel elements
        lst_1 = [4]
        lst_2 = [5]
        res = getDiffOfMean(lst_1, lst_2)
        self.assertEqual(-1, res)    


    def test_empty_list(self):
        #empty lists should raise ValueError
        lst_1 = [4,6,7]
        lst_2 = []
        self.assertRaises(ValueError, getDiffOfMean, lst_1, lst_2)


    def test_getMeanDiffListForAll_1(self):

        lst1 = [1,2]
        lst2 = [3,4]

        val = [-2.0, -1.0, 0.0, 0.0, 1.0, 2.0]

        mdiff = getMeanDiffListForAllPermutations(lst1, lst2)
        print(mdiff)
        self.assertEqual(mdiff, val)

    def test_getMeanDiffListForAll_2(self):

        lst1 = [(1, 0.0001), (2, 0.0001)]
        lst2 = [(3, 0.0001), (4, 0.0001)]

        val = [-2.0, -1.0, 0.0, 0.0, 1.0, 2.0]

        mdiff = getMeanDiffListForAllPermutations(lst1, lst2)
        print(mdiff)
        self.assertEqual([np.round(e) for e in mdiff], val)


    def test_getDiffOfMeanRandomized(self):
        
        lst1 = [(4, 0.0001), (4, 0.001)]
        lst2 = [(1, 0.0001), (1, 0.001)]

        mdiffs = [getDiffOfMeanRandomized(lst1, lst2) for _ in range(500)]
        print(np.mean(mdiffs))

        self.assertTrue(3.0 != np.mean(mdiffs))
        self.assertTrue(np.mean(mdiffs) > 2.95)
        self.assertTrue(np.mean(mdiffs) < 3.05)






            