
## On the Effect of Initialization: The Scaling Path of 2-Layer Neural Networks
Sebastian Neumayer, Lénaïc Chizat, Michael Unser
Keywords: 
JMLR/2024/Proceedings/230549 - On the Effect of Initialization: The Scaling Path of 2-Layer Neural Networks.pdf
Project URL: nan

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[8]

The authors provide a link for the implementation they use regarding the simulations in footnote 2. No implementation given.

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[1]

(2/2)

The authors use the variational problem and give the formula in 43 and 67 but also the unbalanced optimal transport which is given in 68/69. Parameter settings specified in 4.1. The authors specify the package they used for the evaluation.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[1]

The authors vary the value of parameter beta in table 2 and figure 3 which they use for SGD. No other parameters specified.

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[1]

The authors vary the parameter alpha in their experiments for the problem. Evaluations are over the loss maps.

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[10]

Requries expertise on SGD/optimisation and NNs.
