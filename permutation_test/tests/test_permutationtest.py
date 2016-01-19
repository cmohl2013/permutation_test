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
        self.assertTrue(False)    