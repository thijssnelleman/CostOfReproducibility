
## Enhancing Size Generalization in Graph Neural Networks through Disentangled Representation Learning
Zheng Huang, Qihui Yang, Dawei Zhou, Yujun Yan
Keywords: 
ICML/2024/Proceedings/35203 - Enhancing Size Generalization in Graph Neural Networks through Disentangled Representation Learning.pdf
Project URL: nan

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[2]

The authors share a link to their implementation (https://github.com/GraphmindDartmouth/DISGEN). In the readme they state installation instructions, examples on how to execute the code under various parameters and where the output can be found. The file structure is easy to oversee. The code needs more comments.

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[1]

(4/4)

The authors use four datasets, provide citations on them, and state lengthy descriptions with metrics in appendix B and table 5/6. The datasets are not included in the implementation. The data preprocessing scripts are included and explained in appendix C, which negates this cost in large parts thus reducing it.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[1]

The authors show the impact of their hyperparameters in the appendixb in table 7 and 8 (grid search). Hyperparmaeter values of the backbone gnns are als ogives (less relevant). 

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[1]

The authors state the data split in 4.1. and appendix C. The evaluation metric is F1. The results are reported as average plus standard deviation on the small and large test set. The process is repeated 5 times. 

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[5]

Requires expetise on GNN/geometrical deep learning.
