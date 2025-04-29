
## Optimal Goal-Reaching Reinforcement Learning via Quasimetric Learning
Tongzhou Wang, Antonio Torralba, Phillip Isola, Amy Zhang
Keywords: 
ICML/2023/Proceedings/25043 - Optimal Goal-Reaching Reinforcement Learning via Quasimetric Learning.pdf
Project URL: https://www.tongzhouwang.info/quasimetric_rl/

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[1]

The authors provide a link to their implementation (https://github.com/quasimetric-learning/quasimetric-rl/). In the repository they introduce the method and refer to the project page for more, provide installation details and requirements, explain the code file structure, present exampels on how to run. The code has an ok amount of comments but some files its definitely sparse.

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[2]

(3/3)

The authors use three simulators for which they provide citations, mention adaptation in appendix C and provide code for in their implementation. Descriptions on the task are missing.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[4]

The authors summarise the hyperparameter values and architectures in the appendix per simulator. A full overview of hyperparameters is given (only informally). No acquisition strategy specified.

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[1]

The authors report the mean and standard deviation over 5 seeds, with success rate and episodic return (environment measure) as metric.

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[5]

Requires experience with RL.
