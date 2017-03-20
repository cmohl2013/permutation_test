from unittest import TestCase
from ..functions import calc_bin_number
from ..functions import getHistogramFreqAndCenters
from ..functions import getBinWidth
from ..functions import getHistForDatWithErr
import numpy as np

class TestHistogramFunctions(TestCase):
    def test_calc_bin_number(self):
        
        data = [1,1,1,1]
        res = calc_bin_number(data)
        self.assertEqual(res,1,'if all input values are identical, bin_nr should be 1')


    def test_getHistogramFreqAndCenters(self):


        data = [1,1,1,1]
        freq, bin_centers, edges = getHistogramFreqAndCenters(data)
        
        print('freq: ' + str(freq))
        print('bin_centers: ' + str(bin_centers))
        print('bin_edges: ' + str(edges))
        self.assertEqual(len(freq),3)
        self.assertEqual(len(bin_centers),3)

        self.assertEqual(freq[1],1.)
        self.assertEqual(bin_centers[1],1.)
        #self.assertTrue(False)

    def test_getHistogramFreqAndCenters_2(self):

        edges_in = [-0.5, 0.5, 1.5, 2.5]
        data = [1,1,1,1]
        freq, bin_centers, edges = getHistogramFreqAndCenters(data\
                                      , bin_edges=edges_in)
        
        print('freq: ' + str(freq))
        print('bin_centers: ' + str(bin_centers))
        print('bin_edges: ' + str(edges))
        self.assertEqual(len(freq),3)
        self.assertEqual(len(bin_centers),3)

        self.assertEqual(freq[1],1.)
        self.assertEqual(bin_centers[1],1.)
        self.assertEqual(list(edges), edges_in)
        #self.assertTrue(False)    

    def test_getBinWidth(self): 

        centers = [1,2,3,4,5]

        self.assertEqual(1.,getBinWidth(centers))

    def test_getBinWidth_onlyOneBin(self): 

        centers = [3]

        self.assertEqual(1.,getBinWidth(centers)) 



    def test_getHistDatForDataWithErr(self):
    

        lst1 = [(4, 0.0001), (4, 0.001)]
        lst2 = [(1, 0.0001), (1, 0.001)]
        #meandiff is ca 3

        edges = [0,1,2,3,4,5]

        freq, cntr, edge_out = getHistForDatWithErr(lst1, lst2\
                                   , edges)

        print('freq: ' + str(freq))
        print('bin_centers: ' + str(cntr))
        print('bin_edges (out): ' + str(edge_out))
        print('bin_edges (in): ' + str(edges))

        self.assertEqual(edges, list(edge_out))
        self.assertEqual([0.5, 1.5, 2.5, 3.5, 4.5], list(cntr))
        self.assertTrue(freq[1]==0)
        self.assertTrue(freq[2]>0)
        self.assertTrue(freq[3]>0)






