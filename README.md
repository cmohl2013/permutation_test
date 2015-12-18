# permutation_test

## What is it

Implementation of Fisher's permutation test.

```sh
permutation_test(data, ref_data, detailed=False, n_combinations_max=20000, verbose=True)
```

If the number of possible combinations is grater than n_combinations_max,
a random subsample of size n_combinations_max is taken for histogram calculation.

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



According to following publications:

Fisher, R. A. (1935). The design of experiments. 1935. 
Oliver and Boyd, Edinburgh.

Ernst, M. D. (2004). Permutation methods: a basis for exact inference. 
Statistical Science, 19(4), 676-685


## How to install it

```sh
pip install permutation_test
```

## Example
```sh
>>> import permutation_test as p
>>> data = [1,2,2,3,3,3,4,4,5]

>>> p_value = p.permutation_test(data, ref_data)
taking random subsample of size 20000 from 48620 possible permutations
nr of mean diffs: 20000


 Distribution of mean differences
                                       │                                        
                                    *  ┼+1.73038                                
                                       │  *                                     
                                       │                                        
                                 *     │      *                                 
                                       │                                        
                              *        │         *                              
                                       │                                        
                                       │                                        
                          *            │             *                          
                                       │                                        
                                       │                                        
                       *               │                *                       
                                       │                                        
                    *                  │                   *                    
                                       │                                        
                *                      │                       *                
         *   *                         ┼+0.037                    *   *         
───┼*****─***─**─***─**─**─***─**─**─**┼**─***─**─***─**─**─***─**─***─*****┼───
    -2.38713                           │                            +2.39919    
mean difference of tested dataset: -2.0
p_value: 0.00345
p_lower_than (probability that mean of test data is not lower than mean of ref data): 0.00345
p_value_greater_than (probability that mean of test data is not greater than mean of ref data): 0.9998
0.0034500000000000121
```

The asccii art plot shows the ditribution of mean differences for the permutations. 
The ascii art plot is done with [AP](https://github.com/mfouesneau/asciiplot), a plotting package by Morgan Fouesneau.

## 