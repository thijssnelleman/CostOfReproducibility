
## One Model, Any CSP: Graph Neural Networks as Fast Global Search Heuristics for Constraint Satisfaction
Jan Tönshoff, Berke Kisin, Jakob Lindner, Martin Grohe
Keywords: Machine Learning: ML: Reinforcement learning, Constraint Satisfaction and Optimization: CSO: Constraint satisfaction, Machine Learning: ML: Sequence and graph learning
IJCAI/2023/Proceedings/0476 - One Model, Any CSP: Graph Neural Networks as Fast Global Search Heuristics for Constraint Satisfaction.pdf

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[2]

The authors provide a link to their implementation (https://github.com/toenshoff/ANYCSP). In the readme they state the requirements for installation, a link to their validation and test data and how to place in their implementation and how to call training and evaluation scripts. Some files have some comments but many have none, making it more difficult to understand the implementation. The configurations are presented in seperate files making it overseeable. In general the implementation docs could use an index on the file structure and the code could use more comments. The paper has an illlustration of the method applying to an instance. There is a section dedicated to the implementation (4.3) in the paper. 

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[1]

(5/5)

The authors link the data used in the paper in their implementation docs. They state in section five a lengthy introduction on each task/dataset with citations. Direct links on the data sets are also provided in the paper.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[2]

The authors state their hyperparameters in 4.3 and refer to appendix A for all parameters but this is missing (Stated that it is to be found in the implementation link but cannot be found). There are full config files present in the implementation. The authors state they 'choose' some of the values, indicating they were selected empirically but no budget is specified.

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[1]

The authors state the train/test splits per dataset in section 5. They evaluate the methods with single runs/models. The metrics used are task/data set specific and explained in the experimental setup.

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[3]

Requires expertise in graph neural networks / geometrical deep learning and constraint satisfaction.
