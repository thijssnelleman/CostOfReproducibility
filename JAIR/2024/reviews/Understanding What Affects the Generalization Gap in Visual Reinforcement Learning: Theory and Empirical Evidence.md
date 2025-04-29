
## Understanding What Affects the Generalization Gap in Visual Reinforcement Learning: Theory and Empirical Evidence
Jiafei Lyu, Le Wan, Xiu Li, Zongqing Lu
Keywords: 
JAIR/2024/Proceedings/16422 - Understanding What Affects the Generalization Gap in Visual Reinforcement Learning: Theory and Empirical Evidence.pdf
Project URL: 

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[1]

The authors evaluate other works to validate their theoretical claims and provide a link to this implementation (https://github.com/nicklashansen/dmcontrol-generalization-benchmark). Since its not their own method being implemented, re-implementation not applicable.

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[3]

(1/1)

The authors use walkerwalk environment from the linked implementation. The environment is not described.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[1]

The authors state they use 'default hyperparameters of these algorithms' in appendix B. This is fine as its not their own method.

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[1]

Each algorithm is evaluated across 100 episodes for 5 different random seeds. The authors measure average representation deviation and average policy deviation (formula given).

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[9]

Requries expertise on RL.
