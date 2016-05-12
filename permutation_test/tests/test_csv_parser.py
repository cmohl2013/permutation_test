from unittest import TestCase
from ..functions import permutationtest
import numpy as np
import pandas as pd
import permutation_test.csv_parser as csv_parser
class TestCsvParser(TestCase):
    

    def test_parse_dataframe(self):

        pdata = {'exp1' : [1, 2, 3, 4]\
                , 'exp2' : [5, 6, 7, 8]\
                , 'treatment' : ['wt', 'mutant', 'wt', 'mutant']}

        df = pd.DataFrame(pdata)        

        val = {'exp1' : { 'wt' : [1, 3], 'mutant' : [2, 4]}\
            , 'exp2' : { 'wt' : [5,7], 'mutant' : [6, 8]}\
            }

        res = csv_parser.parse_dataframe(df, exp_names=['exp1', 'exp2']\
            , treatment_colname='treatment')
        print(res)
        self.assertEqual(res, val)

    def test_parse_dataframe_autoexp(self):

        pdata = {'exp1' : [1, 2, 3, 4]\
                , 'exp2' : [5, 6, 7, 8]\
                , 'treatment' : ['wt', 'mutant', 'wt', 'mutant']}

        df = pd.DataFrame(pdata)        

        val = {'exp1' : { 'wt' : [1, 3], 'mutant' : [2, 4]}\
            , 'exp2' : { 'wt' : [5,7], 'mutant' : [6, 8]}\
            }

        res = csv_parser.parse_dataframe(df, treatment_colname='treatment')
        print(res)
        self.assertEqual(res, val)    

    def test_parse_dataframe_ioerror(self):
        pdata = {'exp1' : [1, 2, 3, 4]\
                , 'exp2' : [5, 6, 7, 8]\
                , 'treatment' : ['wt', 'mutant1', 'wt', 'mutant2']}


        df = pd.DataFrame(pdata)    

        self.assertRaises(IOError,lambda:\
                 csv_parser.parse_dataframe(df, exp_names=['exp1', 'exp2']\
                    , treatment_colname='treatment'))

    def test_parse_dataframe_nonumeric_cols(self):
        pdata = {'exp1' : [1, 2, 3, 4]\
                , 'exp2' : [5, 'heinz', 7, 8]\
                , 'treatment' : ['wt', 'mutant1', 'wt', 'mutant2']}


        df = pd.DataFrame(pdata)    

        self.assertRaises(IOError,lambda:\
                 csv_parser.parse_dataframe(df, exp_names=['exp1', 'exp2']\
                    , treatment_colname='treatment'))    

    def test_get_treatments_from_df(self):
        pdata = {'exp1' : [1, 2, 3, 4]\
                , 'exp2' : [5, 6, 7, 8]\
                , 'treatment' : ['wt', 'mutant', 'wt', 'mutant']}

        df = pd.DataFrame(pdata)

        val = ['mutant', 'wt']

        res = csv_parser.get_treatments_from_df(df, 'treatment')
        print(res)
        self.assertEqual(set(res), set(val))       
            
    def test_init_data_dict(self):
        exp_names = ['exp1', 'exp2', 'exp3']
        treatments = ['wt','mutant']
        d = csv_parser.init_data_dict(exp_names, treatments)    

    def test_are_exp_cols_numeric(self):
        exp_names = ['exp1', 'exp2']
        
        pdata = {'exp1' : [1, 2, 3, 4]\
                , 'exp2' : [5, 6, 7, 8]\
                , 'treatment' : ['wt', 'mutant', 'wt', 'mutant']}
        df = pd.DataFrame(pdata)    
        res = csv_parser.are_exp_cols_numeric(df,exp_names)    
        self.assertTrue(res)


        pdata = {'exp1' : [1, 2, 3, 4]\
                , 'exp2' : [5, 'heinz', 7, 8]\
                , 'treatment' : ['wt', 'mutant', 'wt', 'mutant']}
        df = pd.DataFrame(pdata)    
        res = csv_parser.are_exp_cols_numeric(df,exp_names)    
        self.assertFalse(res)

    def test_dat_from_csv(self):
        
        val = {'exp2':\
                    {'mutant': [10.52631579, 0.0, 2.9411764710000003, 0.0, 0.0]\
                        , 'WT': [0.0, 9.0909090910000003, 23.07692308, 2.0833333330000001]}\
            , 'exp1':\
                    {'mutant': [15.78947368, 4.3478260869999996, 5.8823529410000006, 0.0, 0.0]\
                    , 'WT': [11.11111111, 9.0909090910000003, 23.07692308, 6.25]}\
            , 'exp3':\
                     {'mutant': [5.263157895, 0.0, 2.9411764710000003, 0.0, 0.0]\
                     , 'WT': [0.0, 6.8181818179999993, 15.38461538, 2.0833333330000001]}\
            }

        path = 'permutation_test/test_data/good_data.csv'
        dat = csv_parser.dat_from_csv(path, treatment_colname='treatment')
        print(dat)
        self.assertEqual(dat,val)    
        
    def test_dat_from_csv_ioerror(self):    
        path = 'permutation_test/test_data/bad_data_three_conditions.csv'
        self.assertRaises(IOError\
            , lambda: csv_parser.dat_from_csv(path, treatment_colname='treatment'))
        
        
