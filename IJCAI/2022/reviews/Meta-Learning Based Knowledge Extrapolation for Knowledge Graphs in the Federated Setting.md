
## Meta-Learning Based Knowledge Extrapolation for Knowledge Graphs in the Federated Setting
Mingyang Chen, Wen Zhang, Zhen Yao, Xiangnan Chen, Mengxiao Ding, Fei Huang, Huajun Chen
Keywords: Data Mining: Knowledge Graphs and Knowledge Base Completion
IJCAI/2022/Proceedings/0273 - Meta-Learning Based Knowledge Extrapolation for Knowledge Graphs in the Federated Setting.pdf

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[2]

The authors present a link to their implementation (https://github.com/zjukg/MaKEr). In the readme they state the requirements/dependencies, introduce the method, explain where the datasets can be found and how they are structured and how to run the train script. There are very few comments in the code. Some implementation details are given in 5.1.

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[1]

(2/2)

The authors present the datasets in their implementation. The authors created these from 2 benchmark datasets (for which they provide citations) and explain how they sampled their data set from the sources. These scripts are available in the implementation, and in the full version (linked in implementation) the authors provide more details in appendix C. Statistics on the data set are given in table 2.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[3]

The authors state the hyperparameter values in 5.1 under the implementation details. A full list of parameters can be found in the implementation. The default values there will have to be assumed for values not stated in the paper. No acquisition strategy specified.

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[1]

The authors specify the training sampling in appendix E. The training test splits of the data is specified in table 2. The evaluation metrics are explained in 5.1. Single runs are presented.

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[5]

Requires experience in knowledge graphs and meta learning.
