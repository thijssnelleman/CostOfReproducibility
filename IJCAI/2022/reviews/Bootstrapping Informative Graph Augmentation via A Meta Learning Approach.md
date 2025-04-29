
## Bootstrapping Informative Graph Augmentation via A Meta Learning Approach
Hang Gao, Jiangmeng Li, Wenwen Qiang, Lingyu Si, Fuchun Sun, Changwen Zheng
Keywords: Machine Learning: Self-supervised Learning, Machine Learning: Meta-Learning, Machine Learning: Representation learning, Machine Learning: Sequence and Graph Learning, Machine Learning: Unsupervised Learning
IJCAI/2022/Proceedings/0416 - Bootstrapping Informative Graph Augmentation via A Meta Learning Approach.pdf

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[4]

The authors share a link to their implementation (https://github.com/hang53/MEGA). An example is given on how to run the code without description. Very few comments are present in the code. No overview of the repository structure is given, and although its not too big, this would be usefull. An architecture overview is given in figure 2. 

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[3]

(12/12)

The authors use twelve benchmark data sets, provide citations on them, automatic downloading is provided in the implementation for half of them. Descriptions/statistics are not given. 

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[4]

Some of the hyperparameters are specified in section 4.1, specified on each dataset. The considered parameters are specified in the implementation arguments, but no summary is given per experiment but default values are present. This leaves some ambiguity but also a starting point. No acquisition strategy is specified for the parameters. 

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[2]

The authors refer to a previous work for the experimental protocol (including the data set splits). The authors state in the caption of table 1 that they present the averaged accuracy + std over 10 runs. The other metrics noted in the tables are standard. Details regarding the train/test splits will have to be extracted from the reference.

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[4]

Requires experience in geometrical deep learning.
