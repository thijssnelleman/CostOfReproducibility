
## Learning Neural Set Functions Under the Optimal Subset Oracle
Zijing Ou, Tingyang Xu, Qinliang Su, Yingzhen Li, Peilin Zhao, Yatao Bian
Keywords: 
NeurIPS/2022/Proceedings/54333 - Learning Neural Set Functions Under the Optimal Subset Oracle.pdf
Project URL: 

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[2]

The authors provide a link to their implementation in footnote 1 (https://github.com/SubsetSelection/EquiVSet). In the readme they state the method, installation instructions, the datasets used in the experiments with direct links, and how to run the experiments. Some code files have really good comments but in general its a bit lacking. Pseudo code provided in figure 1 and overview in fig 2.

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[1]

(5/5)

The authors provide direct links for Amazon Baby Registry, CelebA and PDBBind datasets. The authors also use 2 synthetic datasets (2 moons and gaussian mixture) and provide the generators in the code (no parameters applicable) and explain them in sec 6. Each dataset is described in sec 5 and citations are providedm, statistics are given in detail in the appendix.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[4]

Architectures are described per dataset in appendix E.1. The hyperparameters in E.2. The batch size is selected from a grid. Other acquisition not specified. No structured overview.

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[1]

Metrics are stated in sec 6 with formulae. All experiments are over 5 random seeds and reported with mean and std dev. Dataset splits are given in sec 6 and appendix E per dataset.

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[3]

Requires expertise on Neural set functions and oracles.
