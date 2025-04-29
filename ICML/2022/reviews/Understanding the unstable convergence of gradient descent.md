
## Understanding the unstable convergence of gradient descent
Kwangjun Ahn, Jingzhao Zhang, Suvrit Sra
Keywords: 
ICML/2022/Proceedings/16685 - Understanding the unstable convergence of gradient descent.pdf
Project URL: nan

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[10]

The authors do an analysis of the convergence of gradient descent. The code used for this analysis is not shared.

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[6]

(2/2)

The authors use CIFAR-10 and a quadratic loss function they describe in example 4 but do not share the code on. No details given on CIFAR-10.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[3]

The authors state various hyperparmeter values for their networks in each experiments. The most important parameter (step size / learning rate) is given. The architecture is given in epxeriment 1. A full overview of used hyperparameters is not given. Acquisition is not applicable as it is an analysis of various settings.

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[1]

The authors evaluate SGD over various NN models and evaluate the loss for analysis. The presented results are single runs.

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[7]

Requires expertise on optimisation and Gradient Descent.
