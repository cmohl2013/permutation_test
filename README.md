# permutation_test

## Installation

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

## 