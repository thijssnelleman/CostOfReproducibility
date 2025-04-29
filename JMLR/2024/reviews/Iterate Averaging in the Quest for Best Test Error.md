
## Iterate Averaging in the Quest for Best Test Error
Diego Granziol, Nicholas P. Baskerville, Xingchen Wan, Samuel Albanie, Stephen Roberts
Keywords: 
JMLR/2024/Proceedings/211125 - Iterate Averaging in the Quest for Best Test Error.pdf
Project URL: https://github.com/diegogranziol/Gadam

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[2]

The authors provide a link to their implementation on the JMLR website (https://github.com/diegogranziol/Gadam). In the readme they state installation requirements, how to run the code regarding the presented experiments with arguments, acknowledgements regarding other implementations used and references. The code could use more comments.

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[3]

(3/3)

The authors conduct experiments on CIFAR and ImageNet, as well as PTB. Citations provided on all. Descriptions/statistics not given. Code automatically downloads ImageNet and CIFAR but PTB does not seem to be included.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[3]

Hyperparameter tuning is discussed in section 6.1. and they state the grids they searched on. The selected values can be found in the readme of the implementation (structured). Not all acquisition in the HPO is explained some are only stated.

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[4]

The authors evaluate test accuracy on the datasets over various optimisers. They present results on the test set it seems although this is not completely clear ("test error"). Data split not explained. Each experiment is run 3 times and they report mean + std dev.

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[5]

Requries expertise on iterative averaging and deep learning theory.
