
## AdAUC: End-to-end Adversarial AUC Optimization Against Long-tail Problems
Wenzheng Hou, Qianqian Xu, zhiyong yang, Shilong Bao, Yuan He, Qingming Huang
Keywords: 
ICML/2022/Proceedings/17207 - AdAUC: End-to-end Adversarial AUC Optimization Against Long-tail Problems.pdf
Project URL: nan

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[10]

The authors do not share their implementation. Algorithm 1 denotes the method in pseudo code. 

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[4]

(3/3)

The authors use CIFAR-10-LT/100-LT and MNIST-LT as datasets. The constructions from the original datasets is described in 5.2. Citation is given for MNIST. 

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[3]

The authors state the parameters in algorithm 1. The parameter values are stated in C.1. The overview is informally stated. No acquisition specified. 

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[4]

The authors evaluate AUC and 'CE' (robustness, subfield specific but not explained). The results are single run and evaluated on the test set. The data split is not defined.

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[5]

Requires expertise in adversarial learning and robustness.
