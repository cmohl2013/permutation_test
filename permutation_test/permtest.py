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
from functions import benjamini_hochberg_procedure

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
    
    parser.add_argument('-a','--alpha'\
        ,type=str, help='significance level alpha (between 0 and 1)'\
                    +' If not defined, alpha is set to 0.05.')

    parser.add_argument('-m','--multi_comp_corr'\
        ,type=str, help='perform multiple comparison correction with benjamini hochberg procedure yes/no, '\
                    +' If not defined, correction is performed.')

    args = parser.parse_args()

    
    path = args.input_filepath
    treatment_colname = args.treatment_column_name
    exp_names = None
    ref_data_name = args.referencegroup
    data_name = args.testgroup
    alpha = args.alpha
    multi_comp_corr = args.multi_comp_corr

    df = pd.read_csv(path)
    
    if data_name is not None:
        df = df[(df[treatment_colname] == data_name) | (df[treatment_colname] == ref_data_name)]

    #find out data name
    treatment_names = cp.get_treatments_from_df(df, treatment_colname)
    if data_name is None:
        data_name = get_data_name(treatment_names, ref_data_name)

    dat = cp.parse_dataframe(df, exp_names, treatment_colname)
    
    if alpha is None:
        #set default significance level
        alpha = 0.05
    alpha = float(alpha)    
    if multi_comp_corr is None:
        multi_comp_corr = True
    if multi_comp_corr == 'yes':
        multi_comp_corr = True
    if multi_comp_corr == 'no':
        multi_comp_corr = False    

               

    batch_permtest(dat, data_name, ref_data_name
        , verbose=True, alpha=alpha, multi_comp_corr=multi_comp_corr)
    

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


def calc_significance(pvalue_datalist, alpha, multi_comp_corr=True):

    pvals = [ d['p_value'] for d in pvalue_datalist]
    pvals_l = [ d['p_value_lower_than'] for d in pvalue_datalist]
    pvals_g = [ d['p_value_greater_than'] for d in pvalue_datalist]

    if not multi_comp_corr: 
        sig = [pval <= alpha for pval in pvals]
        sig_l = [pval <= alpha for pval in pvals_l]
        sig_g = [pval <= alpha for pval in pvals_g]
    else:
        #with multiple comparisons correction (benjamini hochberg)
        sig = benjamini_hochberg_procedure(pvals, alpha=alpha)
        sig_l = benjamini_hochberg_procedure(pvals_l, alpha=alpha)
        sig_g = benjamini_hochberg_procedure(pvals_g, alpha=alpha)

    for i in range(len(pvalue_datalist)):
        pvalue_datalist[i]['is_significant_difference'] = sig[i]
        pvalue_datalist[i]['is_significantly_lower'] = sig_l[i]
        pvalue_datalist[i]['is_significantly_greater'] = sig_g[i]
    return pvalue_datalist    








def batch_permtest(dat, data_name
    , ref_data_name
    , verbose=True
    , alpha=0.05
    , multi_comp_corr=True):
    
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
        
        result = p.permutationtest(data, ref_data, detailed=True, verbose=verbose)
        result['exp_name'] = exp
        result['alpha'] = alpha
        p_values.append(result)
        print('\n\n\n\n')
    
    
    p_values = calc_significance(p_values, alpha, multi_comp_corr=multi_comp_corr)    
    
    print('\n\n')
    print('===============================')
    print('significance yes/no')
    print('===============================')
    if multi_comp_corr:
        print('multiple comparison correction with Benjamini-Hochberg procedure')
    else:
        print('no multiple comparisons correction!')
    print('\n\n')
          
    
    def bool2str(b):
        if b:
            return 'YES'
        return 'NO'    

    for r in p_values:
        
        print('++++++++++++++++++++++++++++++++++++++++++++')
        print('Experiment: ' + r['exp_name'])
        print('++++++++++++++++++++++++++++++++++++++++++++')
        print('reference group: ' + ref_data_name)
        print('test group: '+ data_name)
        print('alpha: '+ str(alpha))
        print('\n')

        print('significantly different: ' + bool2str(r['is_significant_difference']))
        print('test data greater than referece data: ' + bool2str(r['is_significantly_greater']))
        print('test data lower than referece data: ' + bool2str(r['is_significantly_lower']))
        print('\n\n')

        


    return p_values 



if __name__ == '__main__':
    main()

