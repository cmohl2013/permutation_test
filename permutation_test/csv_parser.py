import pandas as pd 
import numpy as np

#def import_csv_data(path):
#   dat = pd.read_csv(path)

def get_treatments_from_df(df, treatment_colname):
    '''
    returns names of treatments
    '''
    col_names = df.columns.tolist()
    if treatment_colname not in col_names:
        error_str = '''treatment column with name '%s' does not exist, 
        only folllowing columns found: %s''' % (treatment_colname, col_names)
        
        raise IOError(error_str)

    return df[treatment_colname].unique().tolist()


def init_data_dict(exp_names, treatments):
    '''
    inits empty dict for parse_dataframe
    '''
    out = dict.fromkeys(exp_names)
    for key in out.keys():
        out[key] = dict.fromkeys(treatments)
    return out  

def get_exp_names(df,treatment_colname):
    '''
    get list of exp names by removing columns with non numeric values 
    and the treatment colname
    '''    
    df = df.select_dtypes(include=['number'])
    colnames = df.columns.tolist()
    try:
        colnames.remove(treatment_colname)
    except: 
        pass
    return colnames

def are_exp_cols_numeric(df,exp_names):
    return df[exp_names].equals(df[exp_names].select_dtypes(include=['number']))

def parse_dataframe(df, exp_names=None, treatment_colname='treatment'):
    
    if exp_names is None:
        exp_names = get_exp_names(df, treatment_colname)

    if not are_exp_cols_numeric(df,exp_names):
        error_str = 'one or more data columns do not contain numeric data'
        raise IOError(error_str)
        

    treatments = get_treatments_from_df(df, treatment_colname)
    if len(treatments)!=2:
        error_str = 'nr of treatments must be 2, but is %s' % (len(treatments))
        raise IOError(error_str)

    #init empty dict
    out = init_data_dict(exp_names, treatments)
   

    colnames_sel = exp_names.copy()
    colnames_sel.append(treatment_colname) 
    
    df = df[colnames_sel]
    melted = pd.melt(df, value_vars=exp_names, id_vars=[treatment_colname])

    grouped = melted.groupby(['variable', treatment_colname])
    for name, group in grouped:
        exp_name = name[0]
        treatment_name = name[1]

        out[exp_name][treatment_name] = group.value.tolist()
    return out  

    
def dat_from_csv(path, exp_names=None, treatment_colname='treatments'):
    df = pd.read_csv(path)
    return parse_dataframe(df, exp_names, treatment_colname)



