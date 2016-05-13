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
    

    #find out data name
    treatment_names = cp.get_treatments_from_df(df, treatment_colname)
    data_name = get_data_name(treatment_names, ref_data_name)

    dat = cp.parse_dataframe(df, exp_names, treatment_colname)
    batch_permtest(dat, data_name, ref_data_name, verbose=True)
    

def load_data(path, exp_names, treatment_colname):
    df = pd.read_csv(path)
    return cp.parse_dataframe(df, exp_names, treatment_colname)


def get_data_name(treatment_names, ref_data_name):
    if len(treatment_names) != 2:
        print('nr of treatments must be 2, but is %s' % len(treatment_names))
        return
    if ref_data_name not in treatment_names:
        print('ref data name not found: %s' % ref_data_name)
        return

    data_name = treatment_names.copy()
    data_name.remove(ref_data_name)

    return data_name[0]

def batch_permtest(dat, data_name, ref_data_name, verbose=True):
    p_values = []
    
    print('============================================')
    print('permutation test')
    print('============================================')
    print('\n\n\n\n')

    for exp in dat.keys():
        
        print('++++++++++++++++++++++++++++++++++++++++++++')
        print('Experiment: ' + exp)
        print('++++++++++++++++++++++++++++++++++++++++++++')
        print('reference group: ' + ref_data_name)
        print('test group: '+ data_name)
        print('\n')

        ref_data = dat[exp][ref_data_name]
        data = dat[exp][data_name] 
        p_values.append(p.permutationtest(data, ref_data, detailed=True, verbose=verbose))
        print('\n\n\n\n')
    return p_values 
