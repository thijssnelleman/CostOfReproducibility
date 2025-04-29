
## Clustering with Semidefinite Programming and Fixed Point Iteration
Pedro Felzenszwalb, Caroline Klivans, Alice Paul
Keywords: 
JMLR/2022/Proceedings/210402 - Clustering with Semidefinite Programming and Fixed Point Iteration.pdf
Project URL: nan

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[8]

The authors state they implemented the method in Python and use cxpy package as well as scipy library for k-means implementation.  

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[4]

(2/2)

The authors use synthetic data in 6.1 and use MNIST in 6.2 (citation + direct link in reference) and visiualise the dataset in figure 10 of the subset they use which suffices. The synthetic data is described with details in 6.1. bnut no implementation given.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[1]

The parameter of the method is k and is specified for each experiment, varying k over a grid.

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[1]

Table 2 report mean + std dev over 20 trials in table 2. The rand index metric is explained in 6.1 with citation and the experiment is repeated 10 times and they present the min, max and mean of the ratios as well as mean and standard deviation of the accuracy. 

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[8]

Requires experitse with clustering.
