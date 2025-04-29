
## Robust Reinforcement Learning via Progressive Task Sequence
Yike Li, Yunzhe Tian, Endong Tong, Wenjia Niu, Jiqiang Liu
Keywords: AI Ethics, Trust, Fairness: ETF: Safety and robustness, Agent-based and Multi-agent Systems: MAS: Agent theories and models
IJCAI/2023/Proceedings/0051 - Robust Reinforcement Learning via Progressive Task Sequence.pdf

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[8]

The authors state the implementation is available online (https://github.com/li-yike/DRRL). The repository is empty except for a readme. In 4.1 there are details on what has been implemented with citations from which libraries were used. Figure 2 gives an overview of the method, algorithm 1 pseudo code on the method.

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[1]

(3/3)

The authors use simulated environments for their experiments, which they reference a source library used for in 4.1. The environments are seemingly parameterless.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[8]

The authors state their training hyperparameters in 4.1 where the learning rate is fixed and the other hyper-parameters are tuned by grid search but their values are not stated nor is the budget (size of the grid). This leaves a lot of open questions, and makes it very difficult to reproduce let alone defend comparisons.

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[2]

The authors evaluate the methods on each simulation and evaluate it on the mean reward as stated in the illustrations. Some of experiment evaluation requires some expertise to understand, but it is well documented in general.

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[5]

Requires expertise on robustness and RL policies.
