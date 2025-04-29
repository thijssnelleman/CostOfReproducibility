## Reversible and irreversible bracket-based dynamics for deep graph neural networks
Anthony Gruber, Kookjin Lee, Nathaniel Trask
Keywords: 
NeurIPS/2023/Proceedings/72854 - Reversible and irreversible bracket-based dynamics for deep graph neural networks.pdf
Project URL:

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[2]

Code repository is provided.
Pros
- Clear execution commands
Cons
- Dependencies are named in the readme file, but without versions
- Comments are limited
- There are too many unused files and two main code directories (src and src-new)

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[3]

(7/8)

There are 3 main experiments.

Pendulum experiment (cost 3, 25%)
There is no code of the experiment, just a mathmatical description with citation. It is not entirely clear how the double pendulum is simulated.

MuJoCo experiment (cost 2, 25%)
The simulator is cited, but not linked. It is properly described. There is not a lot of detail on how data collection is done.

Node classification (cost 3, 50%)
Datasets are cited but not linked. The datasets are not described and no statistics are discussed.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[6]

There is a summary of the configurations, a yaml file in the repo, but it is unclear how this is used. Only for the node classification task the hyperparameter settings are clear. There is no description of how the parameters are found nor the budget used.

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[3]

The metrics used are clear and well-known. It is mostly clear how the train/test/val sets are split. It is only clear for the node classification task how this split is obtained, for the environments it is not clearly provided how training and testing is seperated. It is clear that experiments are repeated and how results are aggregated.

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[7]

The paper is math heavy on difficult topics. It touches on multiple mathmatical disciplines as well as on geometric deep learning and phisycs simulations.