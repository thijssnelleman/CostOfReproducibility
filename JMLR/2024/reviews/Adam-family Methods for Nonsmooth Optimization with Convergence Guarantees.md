
## Adam-family Methods for Nonsmooth Optimization with Convergence Guarantees
Nachuan Xiao, Xiaoyin Hu, Xin Liu, Kim-Chuan Toh
Keywords: 
JMLR/2024/Proceedings/230576 - Adam-family Methods for Nonsmooth Optimization with Convergence Guarantees.pdf
Project URL: nan

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[8]

The authors state the programming language and framework (PyTorch) used with version numbers in 6.2. The implementation is not shared. Pseudo code give in algorithm 1.

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[4]

(2/2)

The authors use CIFAR-10 and CIFAR-100 and provide a citation on them. No descriptions or details otherwise.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[3]

Hyperparameters are stated in 1.3. under formula 1. The authors details their values in 6.1. and state for three they conduct a grid search and provide the grids. The authors are stated to remain their 'default values'. There is no structured overview on the values. The selected values are not always clear.

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[4]

The authors measure accuracy on the test set in figure 1 and test loss as well in figure 4. Each experiment is ran 5 times with different random seeds. The aggregation and variation is not stated. The results are on the test set and it is implied that these are from the datasets but not actually stated.

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[5]

Requires expertise on adam-family methods and optimisation.
