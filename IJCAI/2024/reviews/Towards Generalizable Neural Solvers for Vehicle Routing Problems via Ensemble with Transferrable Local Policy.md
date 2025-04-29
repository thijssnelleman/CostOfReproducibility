
## Towards Generalizable Neural Solvers for Vehicle Routing Problems via Ensemble with Transferrable Local Policy
Chengrui Gao, Haopu Shang, Ke Xue, Dong Li, Chao Qian
Keywords: Search: S: Search and machine learning, Machine Learning: ML: Reinforcement learning, Search: S: Combinatorial search and optimisation
IJCAI/2024/Proceedings/0764 - Towards Generalizable Neural Solvers for Vehicle Routing Problems via Ensemble with Transferrable Local Policy.pdf

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[2]

The authors provide a link to their implementation (https://github.com/lamda-bbo/ELG). In the readme they provide brief instructions on how to generate data, run training and testing. The code has some comments, but in general the implementation could do with some more documentation regarding the structure and how to use the code.  

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[2]

(5/5)

The authors provide data set files in the implementation documentation. Descriptions on the data sets are given, but citations and statistics are missing.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[2]

The authors provide configuration files with complete values in the implementation documentation. The authors refer to the appendix for hyperparameter setting in their paper, which is linked in the acknowledgements. There they provide a table with the settings per problem, and from where they derive the policy values but not all values are clarified how they were determined. A HP sensitivity analysis is done for their newly introduced HPs on a grid. 

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[1]

The authors state the performance metrics in 4.1, and how they are calculated. The training procedures are specified and the training instances are randomly generated (with details on how this is done) and the trained models are then evaluated on the benchmark data sets. The authors present single run results, which is clear given the task.

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[5]

Requires an understanding of many different subfields, mainly RL, in ML in combination with the two NP hard tasks evaluated on.
