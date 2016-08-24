from unittest import TestCase
from ..functions import permutationtest
from ..functions import iter_sample_fast
import numpy as np
from pprint import pprint

class TestPermutationtest(TestCase):
    def test_calculation(self):
        
        lst_1 = [1,2,3]
        lst_2 = [4,5,6]
        res = permutationtest(lst_1, lst_2, verbose=False, detailed=True)
        print(res)
        #self.assertTrue(False)
        #edge histogram values should be zero
        self.assertEqual(res['hist_data'][0][0], 0.) #histogram value (probability)
        self.assertEqual(res['hist_data'][0][-1], 0.) #histogram value (probability)

    def test_identical_values(self):
        
        lst_1 = [1,1,1,1,1,1]
        lst_2 = [1,1,1,1,1]

        res = permutationtest(lst_1, lst_2, verbose=False, detailed=True)
        print(res)
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

        print(res)
        self.assertTrue(res['p_value_lower_than']<0.001)

    def test_separated_values_2(self):
        data = [1.0708668227418792, 1.1067254452875099, 1.0333228407409827\
           , 1.0132937578438619, 1.0231316882566115, 1.0820169073058068\
           , 1.0980227298300425, 1.1009000370589768, 1.0451036498157251\
           , 1.0874385771975277]

        ref_data = [1.3782224181702412, 1.4213230893012634, 1.3509515280166928\
           , 1.2465260516379832, 1.3427785344623244, 1.3444623751041545\
           , 1.3141868823607723, 1.1846082779857812, 1.2070882555573963]  
                
        res = permutationtest(data, ref_data, verbose=True, detailed=True)    
        pprint(res)
        self.assertEqual(res['p_value_greater_than'], 1)
        self.assertEqual(res['p_value_lower_than'], 0)

    def test_separated_values_3(self):
        ref_data = [1.0708668227418792, 1.1067254452875099, 1.0333228407409827\
           , 1.0132937578438619, 1.0231316882566115, 1.0820169073058068\
           , 1.0980227298300425, 1.1009000370589768, 1.0451036498157251\
           , 1.0874385771975277]

        data = [1.3782224181702412, 1.4213230893012634, 1.3509515280166928\
           , 1.2465260516379832, 1.3427785344623244, 1.3444623751041545\
           , 1.3141868823607723, 1.1846082779857812, 1.2070882555573963]  
                
        res = permutationtest(data, ref_data, verbose=True, detailed=True)    
        pprint(res)
        self.assertEqual(res['p_value_greater_than'], 0)
        self.assertEqual(res['p_value_lower_than'], 1)    

    def test_iter_sample_fast(self):
        
        def yrange(n):
            i = 0
            while i < n:
                yield i
                i += 1

        g = yrange(3)
        subsample=iter_sample_fast(g,2)        
        print(list(g))
        print(subsample)
        self.assertTrue(len(subsample)==2)

        g = yrange(3)
        subsample=iter_sample_fast(g,3)
        self.assertTrue(len(subsample)==3)

        g = yrange(3)
        self.assertRaises(ValueError, lambda:iter_sample_fast(g,4))





