
## On the Generalization of Stochastic Gradient Descent with Momentum
Ali Ramezani-Kebrya, Kimon Antonakopoulos, Volkan Cevher, Ashish Khisti, Ben Liang
Keywords: 
JMLR/2024/Proceedings/220068 - On the Generalization of Stochastic Gradient Descent with Momentum.pdf
Project URL: nan

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[10]

Implementation not given.

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[5]

(2/2)

The authors use CIFAR-10 and notMNIST as datasets (citations provided only for CIFAR10). No other details.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[3]

The authors discuss the parameter settings in section 5. There is no structured summary. The authors vary alpha and mu over a grid to optimise in table 1 but not all parameters are explained.

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[3]

The authors evaluate the methods on test error and repeated experiments 5 evaluate average performance. Data split not given. Variance is confidence intervals. 

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[8]

Requires expertise on SGD.
