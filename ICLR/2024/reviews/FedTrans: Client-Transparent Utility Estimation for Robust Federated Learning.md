## FedTrans: Client-Transparent Utility Estimation for Robust Federated Learning
Mingkun Yang, Ran Zhu, Qing Wang, Jie Yang
Keywords: 
ICLR/2024/Proceedings/19141 - FedTrans: Client-Transparent Utility Estimation for Robust Federated Learning.pdf
Project URL: nan

### Implementation
_Given the documentation shared by the authors on a new method, how much effort would it be to re-implement the method from scratch?_

[2]

Authors provide implementation link in footnote 1 of the abstract (https://github.com/Ran-ZHU/FedTrans). Repo has install instructions, where to find main entry point, where to find the configuration and how to change with description on each parameter. Code can use more comments.

### Data
_Given the data description in the documentation, how much effort would it take to either: Find the same data set the authors used, or a similar data set and defend the comparability, or acquire one from scratch?_

[3]

(2/2)

CIFAR10, Fashion-MNIST both cited. Data download in code. No other details.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for obtaining the reported results, and compare them against their computation budget?_

[2]

Hyperparameter values summarised in conf file of implementation. Also summarised in appendix C, set empirically but no acquisition budget given.

### Experimental Procedure
_Given the setup of experiments reported in the work, how difficult is it to set up a new experiment with the same procedure, similar to those presented in the original work?_

[1]

Metrics described in 3.1. reporting the average Top-1 accuracy over 5 random seeds. Over static test set. 

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying solely on the available documentation?_

[4]

-
