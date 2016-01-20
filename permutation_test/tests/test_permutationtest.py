from unittest import TestCase
from ..functions import permutationtest
import numpy as np

class TestPermutationtest(TestCase):
    def test_calculation(self):
        
    	lst_1 = [1,2,3]
    	lst_2 = [4,5,6]

        res = permutationtest(lst_1, lst_2, verbose=False, detailed=True)
        print res
        #self.assertTrue(False)


    def test_identical_values(self):
        
    	lst_1 = [1,1,1,1,1,1]
    	lst_2 = [1,1,1,1,1]

        res = permutationtest(lst_1, lst_2, verbose=False, detailed=True)
        print res
        self.assertEqual(res['p_value_lower_than'], 1)  
        self.assertEqual(res['p_value_greater_than'], 1)
        self.assertEqual(res['p_value'], 1)
        self.assertEqual(res['mean_difference'], 0.)
        self.assertEqual(len(res['hist_data'][0]), 3) # nr of bins
        self.assertEqual(len(res['hist_data'][1]), 3) #nr of bins
        self.assertEqual(res['hist_data'][0][1], 1.) #histogram value (probability)
        self.assertEqual(res['hist_data'][1][1], 0.) #bin position
        self.assertEqual(res['hist_data'][0][0], 0) #histogram value (probability)
        self.assertEqual(res['hist_data'][0][2], 0) #histogram value (probability)
        self.assertEqual(res['hist_data'][1][0], -1.) #bin position
        self.assertEqual(res['hist_data'][1][2], 1.) #bin position


    def test_separated_values(self):
        
        lst_1 = [1,1,1,1,1,1]
        lst_2 = [2,2,2,2,2,2,2]

        res = permutationtest(lst_1, lst_2, verbose=True, detailed=True)    

        print res
        self.assertTrue(False)