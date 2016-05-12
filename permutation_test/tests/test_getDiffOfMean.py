from unittest import TestCase
from ..functions import getDiffOfMean
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