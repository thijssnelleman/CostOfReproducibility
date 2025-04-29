
## On Unbalanced Optimal Transport: Gradient Methods, Sparsity and Approximation Error
Quang Minh Nguyen, Hoang H. Nguyen, Yi Zhou, Lam M. Nguyen
Keywords: 
JMLR/2023/Proceedings/221158 - On Unbalanced Optimal Transport: Gradient Methods, Sparsity and Approximation Error.pdf
Project URL: nan

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[10]

Implementation not given.

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[4]

(2/2)

The authors use synthetic data in 5.1. and state its done with package CVXPY and specify the parameter values but more details would be welcome. In 5.2 they evaluate the method on CIFAR-10 (FMNIST is only in the appendix) and provide a citation. 

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[3]

The authors state the name of the input parameters for the algorithm in algorithm 1, 2, 3 and 4. ε and η are given in sec 5 according to theorem 13. In 5.1 they provide the values for the other parameters but not how they were determined. In section 5.2 they vary the values per experiment. Overview missing.

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[2]

Metrics are primal gap (not explained), wallclock time, sparsity. Single runs presented. Data split not applicable.

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[9]

Requires expertise on unbalanced optimal transport and convex optimization.
