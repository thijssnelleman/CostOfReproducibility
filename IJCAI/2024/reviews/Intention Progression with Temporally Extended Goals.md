
## Intention Progression with Temporally Extended Goals
Yuan Yao, Natasha Alechina, Brian Logan
Keywords: Agent-based and Multi-agent Systems: MAS: Agent theories and models, Agent-based and Multi-agent Systems: MAS: Engineering methods, platforms, languages and tools
IJCAI/2024/Proceedings/0033 - Intention Progression with Temporally Extended Goals.pdf

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[4]

The authors share their implementation (https://github.com/yvy714/TEG-MCTS). The readme is empty. The code has a decent amount of comments and is well structured. There are some notes on the implementation in the paper, but not many explanation is given. This means a lot of reverse engineering can be expected.

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[1]

(1/1)

The authors use a simulated environment for their experiments. They state the parameters of the environment in 5.2. The implementation is given and an example on it in figure 5.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[4]

The authors state the values of the MCTS scheduler in section 5.2, one of which seemingly correspond to algorithm 1. However this is a bit complex to make out, and is also not parametrised in the implementation. 

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[1]

The authors state details on the results in 5.3, such as the number of runs and how performance is aggregated. The metric is 'reward' of the environment / policy, and they show the results over the number of goals in the environment.

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[4]

Requires experience in RL policies.
