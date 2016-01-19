from unittest import TestCase
from ..functions import calc_bin_number
from ..functions import getHistogramFreqAndCenters
from ..functions import getBinWidth
import numpy as np

class TestHistogramFunctions(TestCase):
    def test_calc_bin_number(self):
        
    	data = [1,1,1,1]

        res = calc_bin_number(data)
        
        self.assertEqual(res,1,'if all input values are identical, bin_nr should be 1')


    def test_getHistogramFreqAndCenters(self):


    	data = [1,1,1,1]
    	freq, bin_centers = getHistogramFreqAndCenters(data)
    	
    	self.assertEqual(len(freq),1)
    	self.assertEqual(len(bin_centers),1)

    	self.assertEqual(freq[0],1.)
    	self.assertEqual(bin_centers[0],1.)

    def test_getBinWidth(self): 

    	centers = [1,2,3,4,5]

    	self.assertEqual(1.,getBinWidth(centers))

    def test_getBinWidth_onlyOneBin(self): 

    	centers = [3]

    	self.assertEqual(1.,getBinWidth(centers))	