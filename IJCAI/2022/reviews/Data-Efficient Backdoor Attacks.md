
## Data-Efficient Backdoor Attacks
Pengfei Xia, Ziqiang Li, Wei Zhang, Bin Li
Keywords: Multidisciplinary Topics and Applications: Security and Privacy, AI Ethics, Trust, Fairness: Safety & Robustness
IJCAI/2022/Proceedings/0554 - Data-Efficient Backdoor Attacks.pdf

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[3]

The authors present their implementation online ('prototype code') (https://github.com/xpf/Data-Efficient-Backdoor-Attacks). In the readme they introduce their work and how to run the code with parameter instructions. The code is basically without comments. The directory structure is quite straight forward. The authors provide pseudo code in algorithm 1 in the paper. 

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[3]

(2/2)

The authors state in 4.1 the dataset and a subset of another (the latter is available in the implementation). Both are public. The data sets have a citation provided. Descriptions are given how the subset is created. There is no direct link provided on the first. The descriptions and statistics are missing.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[3]

The authors state the hyperparameters in section 4.1. The hyperparameters of their own method are summarised in algorithm 1. They vary one of these parameters in their experiment shown in figure 3. They specify the values used for the others in 4.1. There is (asside from the mixing ratio parameter in figure 2, and alpha in table 1 as well) no exploration or strategy/budget specified on how the values were acquired.

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[2]

The authors state in figure 3 the experiment is repeated 30 times, and that they present the best runs (aggregation) but the variance is not clarified. The other results are single runs. The metric is attack success rate (Task specific accuracy). 

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[4]

Requires experience with adversarial attacks and robustness in NNs.
