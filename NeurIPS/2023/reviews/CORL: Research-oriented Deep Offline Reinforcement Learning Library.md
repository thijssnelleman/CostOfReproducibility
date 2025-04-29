
## CORL: Research-oriented Deep Offline Reinforcement Learning Library
Denis Tarasov, Alexander Nikulin, Dmitry Akimov, Vladislav Kurenkov, Sergey Kolesnikov
Keywords: 
NeurIPS/2023/Proceedings/73613 - CORL: Research-oriented Deep Offline Reinforcement Learning Library.pdf
Project URL: 

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[1]

The authors provide a link to their implementation (https://github.com/corl-team/CORL). In the readme they provide installation instructions, a list of implemented algorithms and benchmark results. The code has a documentation website which is very extensive. 

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[2]

(9/9)

The authors evaluate datasets from D4RL (citation provided), for the Gym-MuJoCo environments which automatically install with the implementation. The environments are not described. They are evaluated under various settings which are given in the implementation.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[1]

The authors evaluate a lengthy list of baselines in their method. The authors use the hyperparameters from the original works. their values are listed in appendix D.2. They can also be found as config files per experiment in the repository. Acquisition is in this case replacting as the original work.

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[2]

The authors evaluate the methods on the environments over 4 random seeds and average. The performance is environment based. The variance is not explained. Train test split not applicable.

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[2]

Requries expertise in RL.
