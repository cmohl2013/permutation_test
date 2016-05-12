'''
command line script that reads a dataset in csv format and performs
one permuation test per data column.
one additional column defines the population type.
the population column must contain 2 different values
(two populations are tested against each other)
'''
import permutation_test as p
import permutation_test.csv_parser as cp
import pandas as pd

def main():
    treatment_colname='treatment'
    exp_names = None
    ref_data_name = 'WT'
    data_name = 'mutant'
    path = 'permutation_test/test_data/good_data.csv'
    
    df = pd.read_csv(path)
    dat = cp.parse_dataframe(df, exp_names, treatment_colname)

    #find out data name
    treatment_names = cp.get_treatments_from_df(df, treatment_colname)
    data_name = treatment_names.copy()
    data_name.remove(ref_data_name)
    data_name = data_name[0]

    for exp in dat.keys():
        print('ref_data')
        print(ref_data_name)
        print('data')
        print(data_name)
        ref_data = dat[exp][ref_data_name]
        data = dat[exp][data_name] 
        p_value = p.permutationtest(data, ref_data, detailed=True)
    print(p_value)