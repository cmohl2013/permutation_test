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
import argparse

def main():
    
    parser = argparse.ArgumentParser()
    
    parser.add_argument('input_filepath'\
        ,type=str, help='e.g. path/to/my/data.csv, path to csv file with data')
    parser.add_argument('treatment_column_name'\
        ,type=str, help='name of column in the csv table that specifies the groups')
    parser.add_argument('referencegroup'\
        ,type=str, help='name of the reference group as named in the csv table')
    
    parser.add_argument('-t','--testgroup'\
        ,type=str, help='name of the test group as named in th csv table.'\
                    +' If not defined, test group is determined automatically.')
    args = parser.parse_args()

    
    path = args.input_filepath
    treatment_colname = args.treatment_column_name
    exp_names = None
    ref_data_name = args.referencegroup
    data_name = args.testgroup
    
    
    df = pd.read_csv(path)
    
    if data_name is not None:
        df = df[(df[treatment_colname] == data_name) | (df[treatment_colname] == ref_data_name)]

    #find out data name
    treatment_names = cp.get_treatments_from_df(df, treatment_colname)
    if data_name is None:
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
        print('only following names found:')
        print(treatment_names[0])
        print(treatment_names[1])
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
