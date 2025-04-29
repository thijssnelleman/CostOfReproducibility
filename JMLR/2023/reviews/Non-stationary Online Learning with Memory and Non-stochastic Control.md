
## Non-stationary Online Learning with Memory and Non-stochastic Control
Peng Zhao, Yu-Hu Yan, Yu-Xiang Wang, Zhi-Hua Zhou
Keywords: 
JMLR/2023/Proceedings/220218 - Non-stationary Online Learning with Memory and Non-stochastic Control.pdf
Project URL: nan

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[10]

No implementation given. Four parts of pseudo code specified.

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[8]

(2/3)

The authors use a simulated environment in 6.1. and describe it with distributions and parameters. Implementation not given. In 6.2 they use different environments (LDS and real inverted pendulum latter being called a common environment) but less information is provided and links or citations.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[8]

The authors state the parameters of their method in algorithm 1,2 and 3 but the values are not speicfied in the experiments.

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[1]

Metric is cumulative loss. Results are over five repeated experiments and report the mean + std dev in both 6.1. and 6.2. 

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[9]

Requries expertise on online learning.
