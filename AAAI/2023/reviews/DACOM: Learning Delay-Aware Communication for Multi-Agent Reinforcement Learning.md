
## DACOM: Learning Delay-Aware Communication for Multi-Agent Reinforcement Learning
Tingting Yuan, Hwei-Ming Chung, Jie Yuan, Xiaoming Fu
Keywords: MAS: Agent Communication, ML: Reinforcement Learning Algorithms, ML: Reinforcement Learning Theory, MAS: Multiagent Learning
AAAI/2023/Proceedings/26389 - DACOM: Learning Delay-Aware Communication for Multi-Agent Reinforcement Learning.pdf

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[8]

The authors state their implementation was done in Python 3.6.2 and PyTorch 1.7.1. They present a high level architecture overview in figure 3. No other details can be found.

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[2]

(3/3)

The authors use public simulators and provide direct links on them. Their modifcations regarding 'communication delays' are not given and would have to be re-implemented.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[4]

The authors provide the values of 3 essential hyperparameters and details regarding the architecture. It is not discussed how these values are determined, nor is it clear if all HPs are described.

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[1]

The authors provide clear details on the metrics measured and the settings per environment.

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[6]

Requires a thorough understanding of multi-agent systems, RL and the task presented (communication delays).
