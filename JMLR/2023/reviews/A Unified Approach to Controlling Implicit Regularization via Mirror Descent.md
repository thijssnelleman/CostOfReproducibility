
## A Unified Approach to Controlling Implicit Regularization via Mirror Descent
Haoyuan Sun, Khashayar Gatmiry, Kwangjun Ahn, Navid Azizan
Keywords: 
JMLR/2023/Proceedings/230836 - A Unified Approach to Controlling Implicit Regularization via Mirror Descent.pdf
Project URL: nan

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[4]

The authors do not provide a link to their implementation. The authors state a library they used for their experiment with direct link in appendix I. There is also a code snippit of an implementation in appendix H where they show an implementation using PyTorch. These details are actually very practical and also fulfills the role of pseudo code that this is a -1 (as under point C of the guideline).

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[3]

(3/3)

The authors use MNIST (citation), CIFAR-10 (citation, direct link in the appendix), and and ImageNet experiment in the appendix (ignored). In 4.1 they generated a linearly separable set of 15 point in R^2, which is a straightforward simulation and in R^100 in the second experiment. The description/statistics is a bit lacking on CIFAR-10/MNIST.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[3]

Network architecture is described in 4.2. and appendix I. The authors state the parameters of their own method in section 4 and motivate one theoretically and vary the values of p and B. The step size N is fixed in 4.1. and 4.2 per experiment. Not all parameter values are motivated and a structured overview is missing.

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[1]

The authors evaluate the convergence of their optimiser in the synthetic experiment and evaluate NNs on the test set of CIFAR-10 with mean + std dev over 5 trials in table 4. The authors indicate they use the static test set of the dataset. Metrics are accuracy, training loss, loss and formulae which they define in the paper. 

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[5]

Requires expertise on gradient descent.
