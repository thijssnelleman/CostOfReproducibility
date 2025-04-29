
## Certified Machine Unlearning via Noisy Stochastic Gradient Descent
Eli Chien, Haoyu Wang, Ziang Chen, Pan Li
Keywords: 
NeurIPS/2024/Proceedings/94094 - Certified Machine Unlearning via Noisy Stochastic Gradient Descent.pdf
Project URL: 

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[1]

The authors state packages/frameworks used with versions and citations in N.3. In footnote 3 they provde a link to their method (https://github.com/Graph-COM/SGD_unlearning). In the readme they state installation notes, commands to reproduce the results from specific experiments/figures. a note on parameters and where results are stored. The code has some comments, could be better but no increase. Structure is simple and partially explained.

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[1]

(2/2)

The authors conduct experiments on MNIST and CIFAR10 on which they provide citations and brief descriptions. They are described in more detail in appendix N.2. The code has automatic downloaders implemented (direct link).

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[3]

The hyperparameters and their values per dataset regarding loss function is stated in table 1 of appendix N. In algorithm 1 they state two hyperparameters hat are not delta. Sigma is being varied in one of the experiments (fig 3c) and table 3 but η is not specified seemingly. The arguments per figure are given in the code so it should be extractable. The acquisition of the values is not given.

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[1]

The reported metric is test accuracy and the results are averaged over 100 trials with std dev as variation. Train and test are given in N.2. as static.

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[7]

Requires expertise in SGD and privacy (un)learning.
