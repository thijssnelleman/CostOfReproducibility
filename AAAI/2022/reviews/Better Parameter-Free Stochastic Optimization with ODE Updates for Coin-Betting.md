
## Better Parameter-Free Stochastic Optimization with ODE Updates for Coin-Betting
Keyi Chen, John Langford, Francesco Orabona
Keywords: Machine Learning (ML)
AAAI/2022/Proceedings/20573 - Better Parameter-Free Stochastic Optimization with ODE Updates for Coin-Betting.pdf

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[10]

The authors do not provide a source to their repository. There are no details on the implementation in the paper. Pseudo code on the algorithm is given in the paper. 

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[8]

(22/22)

The authors use many different data sets (21) from two open datasets websites. They do not specify which data sets are used but are clear on how they treat them for aggregation of results purposes. They refer to the appendix for more information about the datasets, but this is missing (AAAI limitations). If this were present the cost would probably be substantially lower.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[5]

The authors specify their strategy on selecting the hyperparameter values. They also state their method 'gaurantees best performance without any parameter tuning' as they present a parameter free optimization  method. They use the validation set to determine the best hyperparameter values. The actual values are not presented, but there are statements regarding 'default values' being used.

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[2]

The authors state how the data is sample for training/validation/testing and they aggregate the results (average) on the test set results per model over all the data sets used. They measure the accuracies on the loss but do not give details on the metric. They do state how the loss is normalised per data set to avoid over representation in the aggregate. They also state how many time experiments are repeated and refer to the appendix for more information

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[4]

The method requires a good understanding on algorithm configuration and parameter optimization.
