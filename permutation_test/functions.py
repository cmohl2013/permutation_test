#import pandas as pd

import numpy as np
import random
import permutation_test.ap as ap
#import warnings
from operator import mul   
from fractions import Fraction
import functools


def permutationtest(data, ref_data, detailed=False, n_combinations_max=20000, verbose=True, n_bins=None):
    ''' 
    Christoph Moehl, Image and Data Analysis Facility, DZNE Bonn, Germany
    christoph.moehl(at)dzne.de

    Implementation of Fisher's permutation test.

    If detailed is False, only (two-sided) p_value is returned,
    i.e. the probability that data is not different from ref_data 

    If detailed is True, one-sided p values and histogram data of 
    mean differences is returned in a dict:

    hist_data: distribution of mean differences for all permutations
    p_value: two sided p_value (the probability that data is not
    different from ref_data )
    p_value_lower_than: the probability that mean of data is not 
    lower than mean of ref_data
    p_value_greater_than: the probability that mean of data is 
    not grater than mean of ref_data


    If the number of possible combinations is grater than n_combinations_max,
    a random subsample of size n_combinations_max is taken for histogram calculation.

    According to following publications:
    
    Fisher, R. A. (1935). The design of experiments. 1935. 
    Oliver and Boyd, Edinburgh.
    
    Ernst, M. D. (2004). Permutation methods: a basis for exact inference. 
    Statistical Science, 19(4), 676-685
    '''
    mean_diff = getDiffOfMean(data, ref_data)
    mean_diffs = getMeanDiffListForAllPermutations(data, ref_data\
                            , n_combinations_max=n_combinations_max)

    print('nr of mean diffs: ' + str(len(mean_diffs)))
    freq, vals = getHistogramFreqAndCenters(mean_diffs, n_bins=n_bins)
    bin_width = getBinWidth(vals)

    cum_freq = np.cumsum(freq) * bin_width #cumulative histogram values
    
    greater_than_index = mean_diff > vals
    lower_than_index = mean_diff < vals
    # print 'greater than index: ' + str(greater_than_index)
    # print 'loweer than index: ' + str(lower_than_index)
    # print 'vals: ' + str(vals)
    # print 'cum_freq: ' + str(cum_freq)
    
    # if not greater_than_index.any():
    #     p_value_greater_than = 1
    # else:
    #     p_value_greater_than = 1-cum_freq[greater_than_index][-1]
        
    # if not lower_than_index.any():
    #     p_value_lower_than = 1  
    # else:
    #     p_value_lower_than = cum_freq[lower_than_index][0]
      
    p_value_lower_than = cum_freq[lower_than_index][0]    
    # print 'cum_freq[lower_than_index] :' + str(cum_freq[lower_than_index])
    p_value_greater_than = 1-cum_freq[greater_than_index][-1]        
    
    p_value = min((p_value_lower_than, p_value_greater_than))



    if verbose:
        p = ap.AFigure()
        print('\n\n Distribution of mean differences')
        print(p.plot(vals, freq, marker = '*'))
        print('mean difference of tested dataset: ' + str(mean_diff))
        print('p_value: ' + str(p_value))
        print('p_lower_than (probability that mean of test data is not lower than mean of ref data): ' + str(p_value_lower_than))
        print('p_value_greater_than (probability that mean of test data is not greater than mean of ref data): ' + str(p_value_greater_than))
    if detailed:
        result = {'hist_data' : (freq, vals)\
                    , 'mean_difference' : mean_diff\
                    , 'p_value' : p_value\
                    , 'p_value_lower_than' : p_value_lower_than\
                    , 'p_value_greater_than' : p_value_greater_than\
                    }
        return result
   
    return p_value               


def getBinWidth(vals):
    if len(vals)<2:
        return 1
    return vals[1]-vals[0]

# def getPermutations(lst, num=None):
    
#   if num is None:
#       return list(itertools.permutations(lst, len(lst)))
#   return  list(itertools.permutations(lst, num))
        
def getDiffOfMean(lst_1, lst_2):
    '''
    result = mean(lst_1) - mean(lst_2)
    '''
    
    if (len(lst_1)==0) or (len(lst_2)==0):
        raise ValueError('empty list') 

    out = np.nanmean(lst_1) - np.nanmean(lst_2)
    if np.isnan(out):
        raise ValueError('one or more of the average values are NaN')
    return out
    

def getMeanDiffListForAllPermutations(lst_1, lst_2, n_combinations_max = 20000):
    '''
    lst_1 and lst_2 are fused and from all possible permutations, 
    mean differences are calculated.
    '''
    perms = getPerms(lst_1 + lst_2, len(lst_1), n_combinations_max=n_combinations_max)
    mean_diffs = [getDiffOfMean(perm[0], perm[1]) for perm in perms]
    return mean_diffs

def permutations(n, g):
    '''
    returns a generator of permutations

    n : number of elements (integer)
    g : list of values to permute 

    example:
    In [27]: import permutation_test as p
    In [28]: perm_generator = p.permutations(3,[10,11,12,13])
    In [29]: perms = list(perm_generator)
    In [30]: perms
    Out[30]: [[10, 11, 12], [10, 11, 13], [10, 12, 13], [11, 12, 13]]
    '''

    if n == 0:
        yield []

    for j, x in enumerate(g):
        for v in permutations(n-1, g[j+1:]):
            yield [x] + v


def getPerms(dat, n_of_group_a, n_combinations_max = 20000):
    '''
    combined permutation for 2 lists 

    dat: list to be permuted
    n_of_group_a: index for splitting the list

    If nr of possible combinations exceeds n_combinations_max, a random subsample
    of size n_combinations_max is chosen.

    example:
    In [33]: p.getPerms([1,2,3,4,5],3)
    Out[33]: 
    [(array([1, 2, 3]), [4, 5]),
     (array([1, 2, 4]), [3, 5]),
     (array([1, 2, 5]), [3, 4]),
     (array([1, 3, 4]), [2, 5]),
     (array([1, 3, 5]), [2, 4]),
     (array([1, 4, 5]), [2, 3]),
     (array([2, 3, 4]), [1, 5]),
     (array([2, 3, 5]), [1, 4]),
     (array([2, 4, 5]), [1, 3]),
     (array([3, 4, 5]), [1, 2])]

    '''
    

    dat_index = range(len(dat)) 
    
    #nr of possible combinations
    n_combinations = nCk(len(dat_index), n_of_group_a)

    if n_combinations < n_combinations_max:
        perm_list = list(permutations(n_of_group_a, dat_index))
    else:
        perms_iter = permutations(n_of_group_a, dat_index)
        print('taking random subsample of size %s from %s possible permutations' % (n_combinations_max, n_combinations))
        perm_list = iter_sample_fast(perms_iter, n_combinations_max)
            

    combi = []
    for perm in perm_list:  
        group_b = [dat[i] for i in dat_index if not i in perm]
        if len(group_b) == 0:
            raise('gp')
        dat_np = np.array(dat)
        group_a = dat_np[perm]
        combi.append((group_a, group_b))
    return combi    


def calc_bin_number(data):
    '''
    optimal bin number according to Freedman-Diaconis rule
    '''
    
    if len(np.unique(data))==1:
        #if all values in the dataset are identical
        return 1

    #inter quartile range
    iqr = np.percentile(data, 75) - np.percentile(data, 25) 
    
    n = len(data)
    h = 2 * iqr/(float(n)**(1.0/3.0)) #bin width

    n_bins = int(round((max(data) - min(data))/h))
    # print 'n: ' + str(n)
    # print 'iqr: ' + str(iqr)
    # print 'n bins: ' + str(n_bins)
    return n_bins



def getHistogramFreqAndCenters(data, n_bins=None):
    '''
    calculation of histogram (frequency and bin positions) with auto bin number
    '''
    
    if n_bins is None:
        n_bins = calc_bin_number(data)
    
    if n_bins < 10:
        warn_message = \
        'WARNING: Bin number is only %s : statistical analysis might be affected.' % n_bins
        print(warn_message)
        #warnings.warn(warn_message, UserWarning)
        

    freq, bin_edges = np.histogram(data\
                        , bins=n_bins\
                        , normed=True)
    
    freq = np.concatenate([[0],freq,[0]])
    
    bin_width = getBinWidth(bin_edges)
    bin_edge_lowest = bin_edges[0] - bin_width 
    bin_edge_highest = bin_edges[-1] + bin_width 

    bin_edges = np.concatenate([[bin_edge_lowest],bin_edges,[bin_edge_highest]])


    bin_centers = np.diff(bin_edges)/2 + bin_edges[:-1]
    return (freq, bin_centers)



def iter_sample_fast(iterable, samplesize):
    '''
    random subsampling from iterator

    code snippet copied from DzinX on StackOverflow:
    http://stackoverflow.com/questions/12581437/python-random-sample-with-a-generator
    '''

    results = []
    iterator = iterable#iter(iterable)
    # Fill in the first samplesize elements:
    try:
        for _ in range(samplesize):
            results.append(iterator.next())
    except StopIteration:
        raise ValueError("Sample larger than population.")
    random.shuffle(results)  # Randomize their positions
    for i, v in enumerate(iterator, samplesize):
        r = random.randint(0, i)
        if r < samplesize:
            results[r] = v  # at a decreasing rate, replace random items
    return results



def nCk(n,k): 
    '''
    calculate number of combinations 'n over k' (binomial coefficient)
    '''
    return int( functools.reduce(mul, (Fraction(n-i, i+1) for i in list(range(k))), 1) )


