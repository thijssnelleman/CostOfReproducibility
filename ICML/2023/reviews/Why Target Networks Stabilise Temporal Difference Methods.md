
## Why Target Networks Stabilise Temporal Difference Methods
Mattie Fellows, Matthew Smith, Shimon Whiteson
Keywords: 
ICML/2023/Proceedings/23599 - Why Target Networks Stabilise Temporal Difference Methods.pdf
Project URL: nan

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[9]

The authors do not share their implementation. They state the source of the simulators used in the appendix, giving a sort of starting point.

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[1]

(2/2)

The authors use two simulations, one which is very simplistic and another for which they refer to another work. Both are described in details (partially in appendix C). 

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[2]

The hyperparmaters for the second experiment are stated in appendix C table 1. They state the parameters were optimised by grid search, but do not specify grids/budgets.

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[1]

The authors measure loss in figure 2 and reward in figure 3 over the steps in the environments. No split applicable. The experiments were repeated over 5 random seeds aggregated by mean and reporting the standard error.

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[4]

Requires expertise in RL.
