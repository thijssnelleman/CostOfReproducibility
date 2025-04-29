
## Resource-Aware Federated Self-Supervised Learning with Global Class Representations
Mingyi Li, Xiao Zhang, Qi Wang, Tengfei LIU, Ruofan Wu, Weiqiang Wang, Fuzhen Zhuang, Hui Xiong, Dongxiao Yu
Keywords: 
NeurIPS/2024/Proceedings/95354 - Resource-Aware Federated Self-Supervised Learning with Global Class Representations.pdf
Project URL: 

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[3]

The authors provide a link to their implementation in section 1 (https://github.com/limee-sdu/FedMKD). In figure 2 an overall framework on the method is given. In the readme they state what their code was based on and where the entry point can be found. No installation instructions given. The code has few comments. Repo structure is easy to oversee.

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[3]

(2/2)

The implementation has automatic downloading implemented for CIFAR10, CIFAR100, FEMNIST and Shakespeare, only the former two are used. Citations are provided for the CIFAR datasets in 5.1. No descriptions on the data or statistics given.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[3]

The hyperparameter values are stated in appendix C.2. Hyperparameter anaylsis is done in appendix D where they conduct grid search. A full overview is missing on the acquisition.

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[2]

The authors train of CIFAR-10 and 100 and state how they are used in 5.1. inlcuding their static test sets. In some experiments the testing set is specified as target but not everywhere. The metrics areaccuracy over various settings of the data.

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[4]

Requires expertise in federated learning and global representation learning.
