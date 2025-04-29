
## Generalized Ambiguity Decomposition for Ranking Ensemble Learning
Hongzhi Liu, Yingpeng Du, Zhonghai Wu
Keywords: 
JMLR/2022/Proceedings/20843 - Generalized Ambiguity Decomposition for Ranking Ensemble Learning.pdf
Project URL: nan

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[10]

Implementation not given.

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[1]

(4/4)

The authors use four datasets and provide direct links for all (amazon datasets share the same link). They are described with statistics. 

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[2]

The authors provide pseudo code in algorithm 1 for parameter learning. There they state various hyperparameters. They state in 5.2.1 they use the training set for learning the parameters of ensemble models, test set for performance evaluation. They also state 20% of the training set is used as validation set for hyper-parameter selection. The parameters of their own model are specified per dataset informally in 5.2.1 (acquisition not applicable persay as they use this to acquire other HPs). Structured overview missing. They also do an ablation study in sec 5.

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[1]

The authors state the evaluation metrics with formulas in 5.1. Datasets are each randomly split 80/20 for t/t. Results are presented as the average over five runs with random initialisations of the model parameters.

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[8]

Requries expertise on ensemble learning.
