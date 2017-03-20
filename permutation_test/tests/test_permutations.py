from unittest import TestCase
from ..functions import permutations\
                      , getPerms\
                      , check_data_format\
                      , randomize_permutation_data\
                      , is_list_of_tuples
import numpy as np
from pprint import pprint
class TestPermutations(TestCase):
    def test_getPerms(self):

        data = [(1,1),(2,2) ,(3,3),(4,4),(5,5)]

        n = 2

        res = getPerms(data, n)
        pprint(res)
        

        val = \
        [([(1, 1), (2, 2)], [(3, 3), (4, 4), (5, 5)]),\
         ([(1, 1), (3, 3)], [(2, 2), (4, 4), (5, 5)]),\
         ([(1, 1), (4, 4)], [(2, 2), (3, 3), (5, 5)]),\
         ([(1, 1), (5, 5)], [(2, 2), (3, 3), (4, 4)]),\
         ([(2, 2), (3, 3)], [(1, 1), (4, 4), (5, 5)]),\
         ([(2, 2), (4, 4)], [(1, 1), (3, 3), (5, 5)]),\
         ([(2, 2), (5, 5)], [(1, 1), (3, 3), (4, 4)]),\
         ([(3, 3), (4, 4)], [(1, 1), (2, 2), (5, 5)]),\
         ([(3, 3), (5, 5)], [(1, 1), (2, 2), (4, 4)]),\
         ([(4, 4), (5, 5)], [(1, 1), (2, 2), (3, 3)])]\


        self.assertEqual(res,val)
        
    def test_check_data_format_1(self):

        dat = \
        [([(1, 1), (2, 2)], [(3, 3), (4, 4), (5, 5)]),\
         ([(1, 1), (3, 3)], [(2, 2), (4, 4), (5, 5)]),\
         ([(1, 1), (4, 4)], [(2, 2), (3, 3), (5, 5)])]


        self.assertEqual(check_data_format(dat),2)


    def test_check_data_format_2(self):

        dat = \
        [([1, 2], [3, 4, 5]),\
         ([1, 3], [2, 4, 5]),\
         ([1, 4], [2, 3, 5])]


        self.assertEqual(check_data_format(dat),1)

    def test_check_data_format_3(self):

        dat = \
        [([1, 2], [3, 4, 5]),\
         ([1, 3], [(2, 2), 4, 5]),\
         ([1, 4], [2, 3, 5])]


        self.assertEqual(check_data_format(dat),0)

    def test_check_data_format_4(self):

        dat = \
        [([1, 2], [3, 4, 5]),\
         ([1, 3], [2, 4, 5],[3,2]),\
         ([1, 4], [2, 3, 5])]


        self.assertEqual(check_data_format(dat),0)


    def test_randomize_permutation_data(self):
        dat = ([(1, 0.01), (2, 0.01)], [(3, 0.01), (4, 0.01), (5, 0.01)])
        val = ([1., 2.], [3., 4., 5.])

        res = randomize_permutation_data(dat)
        pprint(dat)
        pprint(res)
        #self.assertEqual(res, val)

    def test_is_list_of_tuples_1(self):
        a =  [(1,2), (3,4), (5,6)]

        self.assertTrue(is_list_of_tuples(a))

    def test_is_list_of_tuples_2(self):
        a =  [(1,2), (3,4,4), (5,6)]

        self.assertFalse(is_list_of_tuples(a))

    def test_is_list_of_tuples_3(self):
        a =  [1,2,3,4]

        self.assertFalse(is_list_of_tuples(a))         
                         

