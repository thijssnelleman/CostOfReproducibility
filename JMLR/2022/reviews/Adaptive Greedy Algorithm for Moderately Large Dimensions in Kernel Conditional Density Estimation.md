
## Adaptive Greedy Algorithm for Moderately Large Dimensions in Kernel Conditional Density Estimation
Minh-Lien Jeanne Nguyen, Claire Lacour, Vincent Rivoirard
Keywords: 
JMLR/2022/Proceedings/210582 - Adaptive Greedy Algorithm for Moderately Large Dimensions in Kernel Conditional Density Estimation.pdf
Project URL: nan

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[9]

The authors state their method is implemented in R in 4.3.1. No implementation given.

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[6]

(1/1)

The authors conduct simulation studies in section 4. and describe the distribution and its parameters in 4.1. and the values of the parameters. Implementation not given.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[1]

The authors tune parameters in section 4.2.1 and 4.2.2. They state the fixed value of the other parameter in both before conducting the search. In 4.2.1 the parameter C is rejected for optimisation by theoretical analysis. They optimise a on a grid and evaluate it over variety of sample sizes optimising the absolute error. The results can be found in figure 3 and the authors settle on the value of a = log(d-1). In figure 4 they present the grid of beta and the results and settle on 0.8 for the rest of the experiments. This covers all the parameters described in algorithm 1.

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[1]

The authors evaluate the method on the simulations measuring runtime in an uncaptioned table on page 21, cond. density in figure 5 (eq. 15) over a sample size of 100k. Split not applicable. In figure 8 they add irrelevant variables and show the boxplot over 50 samples.

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[9]

Requries expertise on kernels and conditional density.
